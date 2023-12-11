from channels.db import database_sync_to_async
from rest_framework_simplejwt.authentication import JWTAuthentication

from chat.api.serializers import ChatMessageSerializer
from chat.models import ChatMessage
from core.models import User


@database_sync_to_async
def get_user(raw_token):
    auth = JWTAuthentication()
    validated_token = auth.get_validated_token(raw_token)
    return auth.get_user(validated_token)


@database_sync_to_async
def save_message(data, user: User):
    ser = ChatMessageSerializer(data=data)
    ser.is_valid()
    message = ChatMessage.objects.create(
        sent_by=user,
        read_by_staff=True,
        **ser.validated_data,
    )
    return ChatMessage.objects.select_related("chat").filter(id=message.id).first()
