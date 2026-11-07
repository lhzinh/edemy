from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework import routers, viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="user")
