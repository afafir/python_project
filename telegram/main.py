from pyrogram import Client, filters
from pyrogram.types import Message as TGMessage

from api import MessageAPI
from schemas import Message
from config import settings

app = Client("local_session")
with MessageAPI() as api:
    @app.on_message(filters.incoming & filters.private)
    async def on_message(client: Client, message: TGMessage):
        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''

        await client.add_contact(
            message.from_user.id,
            first_name=first_name,
            last_name=last_name
        )
        message = Message(
            messenger='TELEGRAM',
            text=message.text or '',
            extra_data=dict(
                user_id=message.chat.id,
                first_name=first_name,
                last_name=last_name
            )
        )
        api.send_message(message)

print('Starting Telegram Bot')
app.run()
