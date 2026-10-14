import typing

from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


class SyncUserData:
    "Handle Clerk webhook user events"

    @staticmethod
    async def handle_user_updated_or_created(data: dict) -> tuple[User, bool]:
        "Handle user creation and updates"

        email_addresses = typing.cast(list[dict[str, str]], data.get("email_addresses"))
        email = next(
            (
                address.get("email_address")
                for address in email_addresses or []
                if address.get("id") == data.get("primary_email_address_id")
            ),
            None,
        )

        obj, created = await User.objects.aupdate_or_create(
            clerk_id=data["id"],
            defaults={
                "email": email,
                "username": data.get("username", ""),
                "first_name": data.get("first_name"),
                "last_name": data.get("last_name"),
            },
        )
        return obj, created

    @staticmethod
    async def handle_user_deleted(clerk_id: str) -> None:
        "Handle user deletion with GDPR compliance options"

        @sync_to_async(thread_sensitive=True)
        def _delete_or_deactivate() -> None:
            with transaction.atomic():
                user = (
                    User.objects.select_for_update().filter(clerk_id=clerk_id).first()
                )
                if user is None:
                    return

                has_business_data = user.posts.exists() or user.comments.exists()
                if has_business_data:
                    user.is_active = False
                    user.save(update_fields=["is_active"])
                else:
                    user.delete()

        await _delete_or_deactivate()
