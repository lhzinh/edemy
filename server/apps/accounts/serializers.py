from accounts.models import User
from core.serializers import GeneralSerializer


class UserSerializer(GeneralSerializer):
    class Meta:
        model = User
        fields = "__all__"
