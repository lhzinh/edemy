import inngest.django
from accounts.functions import sync_user
from django.contrib.auth import get_user_model
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from config.client import inngest_client

User = get_user_model()


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "avatar")


# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.filter(clerk_id=self.request.user.id)


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    inngest.django.serve(
        inngest_client,
        [sync_user],
    ),
]
