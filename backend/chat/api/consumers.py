from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework_simplejwt.exceptions import (
    InvalidToken,
    AuthenticationFailed,
)

from chat.api.ws_utils import get_user, save_message
from chat.tasks import send_message_task


class ChatConsumer(AsyncJsonWebsocketConsumer):
    groups = ["broadcast"]

    async def receive_json(self, content, **kwargs):
        if not self.scope.get("user"):
            await self.handle_auth(content.get("token"))
            return

        message = await save_message(content, self.scope["user"])
        send_message_task.delay(
            message.chat.extra_data["user_id"],
            message.text,
            message.chat.messenger,
        )
        data_to_send = dict(
            text=message.text,
            chat_id=message.chat_id,
            local=bool(message.sent_by_id),
            sent_at=message.created_at.isoformat(),
            messenger=message.chat.messenger,
        )
        await self.channel_layer.group_send(
            "broadcast", {"type": "chat.message", "message": data_to_send}
        )

    async def chat_message(self, event):
        await self.send_json(event)

    async def handle_auth(self, token):
        try:
            self.scope["user"] = await get_user(token)
        except (InvalidToken, AuthenticationFailed):
            await self.send_json(dict(error="Auth failed"), close=True)
