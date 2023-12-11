from rest_framework.fields import CharField
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as DRFTokenObtainPairSerializer,
)


class TokenObtainPairSerializer(DRFTokenObtainPairSerializer):
    username = CharField(read_only=True)
    first_name = CharField(read_only=True)
    last_name = CharField(read_only=True)
    access = CharField(read_only=True)
    refresh = CharField(read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        return data
