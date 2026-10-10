import warnings
from dataclasses import dataclass

from clerk_backend_api import AuthenticateRequestOptions, authenticate_request
from clerk_backend_api.security.types import AuthErrorReason
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

warnings.filterwarnings("ignore", module="clerk_backend_api")
warnings.filterwarnings("ignore", module="pydantic")


@dataclass
class ClerkUser:
    """Minimal `request.user` for Clerk-authenticated requests.

    Clerk owns the user directory; this object exposes just enough for
    DRF's `IsAuthenticated` permission. If the app also maintains a
    local User row (via Clerk webhooks), look it up by `id` — the Clerk
    `sub` — in the view or a thin helper.
    """

    id: str
    payload: dict
    is_authenticated: bool = True
    is_anonymous: bool = False
    is_active: bool = True

    def __str__(self) -> str:
        return self.id


class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization") or request.META.get(
            "HTTP_AUTHORIZATION"
        )

        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        state = authenticate_request(
            request,
            AuthenticateRequestOptions(
                secret_key=settings.CLERK_SECRET_KEY,
                jwt_key=settings.CLERK_JWT_KEY,
                authorized_parties=settings.CLERK_AUTHORIZED_PARTIES,
                accepts_token=["session_token"],
            ),
        )

        if not state.is_signed_in:
            if state.reason is AuthErrorReason.SESSION_TOKEN_MISSING:
                return None  # no token supplied; DRF treats this as "not attempted"
            raise AuthenticationFailed(
                detail=state.reason.name if state.reason else "unauthorized",
            )

        # pyrefly: ignore [bad-argument-type, unsupported-operation]
        user = ClerkUser(id=state.payload["sub"], payload=state.payload)
        return (user, state)

    def authenticate_header(self, request):
        return "Bearer"
