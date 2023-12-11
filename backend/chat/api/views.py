from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Case, When, F, Value, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from chat.api.serializers import (
    ChatMessageCreateSerializer,
    ChatSerializer,
    ChatMessageListSerializer,
)
from chat.models import ChatMessage, Chat


class ChatMessageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = ChatMessageListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["chat_id"]

    def get_queryset(self):
        qs = ChatMessage.objects.annotate(
            local=Case(
                When(
                    Q(sent_by__isnull=False) | Q(is_auto_generated=True),
                    then=Value(True),
                ),
                default=False,
            )
        )
        return qs

    def get_serializer_class(self):
        if self.action == "create":
            return ChatMessageCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        data = serializer.validated_data
        extra = data.get("extra_data")
        user_id = extra.get("user_id")
        chat, created = Chat.objects.get_or_create(
            extra_data__user_id=user_id,
            messenger=data.get("messenger"),
            defaults=dict(
                title=extra.get("first_name") + " " + extra.get("last_name"),
                extra_data=extra,
            ),
        )
        message = ChatMessage.objects.create(
            text=data.get("text"),
            chat_id=chat.id,
        )
        data_to_send = dict(
            text=message.text,
            chat_id=message.chat_id,
            local=bool(message.sent_by_id),
            messenger=chat.messenger,
            sent_at=message.created_at.isoformat(),
        )
        layer = get_channel_layer()
        send = async_to_sync(layer.group_send)
        send("broadcast", {"type": "chat.message", "message": data_to_send})
        self.generate_answer(message.text, chat.id, chat.messenger)

    def generate_answer(self, question, chat_id, messenger):
        from nlp_answers import get_answer
        answer = get_answer(question)[0][0]
        if not answer:
            return
        message = ChatMessage.objects.create(
            text=answer,
            chat_id=chat_id,
            is_auto_generated=True,
        )
        data_to_send = dict(
            text=f'Сгенерированный ответ: {message.text}',
            chat_id=message.chat_id,
            messenger=messenger,
            sent_at=message.created_at.isoformat(),
        )
        layer = get_channel_layer()
        send = async_to_sync(layer.group_send)
        send("broadcast", {"type": "chat.message", "message": data_to_send})


class ChatViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.prefetch_related("messages")
