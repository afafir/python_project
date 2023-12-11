from vkbottle.bot import Bot, Message

from api import MessageAPI
from config import settings
from schemas import APIMessage

with MessageAPI() as api:
    bot = Bot(token=settings.VK_TOKEN)

    @bot.on.message()
    async def on_message(message: Message):
        user = await message.get_user()
        message_to_send = APIMessage(
            text=message.text,
            messenger='VK',
            extra_data=dict(
                first_name=user.first_name or '',
                last_name=user.last_name or '',
                user_id=message.from_id
            )
        )
        api.send_message(message_to_send)

    bot.run_forever()
