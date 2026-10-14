import inngest
from accounts.services import SyncUserData

from config.client import inngest_client


@inngest_client.create_function(
    fn_id="sync-user-from-clerk",
    trigger=[inngest.TriggerEvent(event="clerk/user.*")],
    singleton=inngest.Singleton(
        key="event.data.id",
        mode="skip",
    ),
    retries=4,
)
async def sync_user(ctx: inngest.Context) -> dict[str, bool]:
    "Handle webhooks with Inngest allow synchronize data from Clerk to database"

    ctx.logger.info(
        "Processing webhook",
        extra={
            "id": ctx.event.id,
            "event_type": ctx.event.name,
            "user_id": ctx.event.data["id"],
        },
    )

    if ctx.event.name in ("clerk/user.created", "clerk/user.updated"):
        await SyncUserData.handle_user_updated_or_created(data=ctx.event.data)
    elif ctx.event.name == "clerk/user.deleted":
        await SyncUserData.handle_user_deleted(ctx.event.data["id"])

    return {"ok": True}
