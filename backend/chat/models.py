from django.db import models

from chat.enums import MessengerType
from core.models import User


class DateTimeFieldsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Chat(models.Model):
    messenger = models.CharField(choices=MessengerType.choices, max_length=16)
    title = models.CharField(default="", max_length=64)
    extra_data = models.JSONField("Данные мессенджера", default=dict)


class ChatMessage(DateTimeFieldsModel):
    sent_by = models.ForeignKey(
        User, models.CASCADE, "sent_messages", null=True, blank=True
    )
    text = models.TextField()
    is_auto_generated = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, models.CASCADE, "messages")
    read_by_staff = models.BooleanField(default=False)
