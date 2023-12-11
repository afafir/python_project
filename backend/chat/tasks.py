import logging
import random
from typing import Dict, Callable

from asgiref.sync import async_to_sync
from django.conf import settings
from vkbottle.bot import Bot as VKBot

from backend.celery import app
from chat.enums import MessengerType
from chat.telegram import TelegramAPI

logger = logging.getLogger(__name__)


async def telegram_send_message(user_id, text):
    logger.info(f'send to telegram {user_id}')
    async with TelegramAPI() as api:
        await api.send_message(user_id, text)


async def vk_send_message(user_id, text):
    bot = VKBot(token=settings.VK_API_TOKEN)
    await bot.api.messages.send(
        peer_id=int(user_id), message=text, random_id=random.randint(1, 2**31)
    )


SOCIALS_MAPPING: Dict[str, Callable] = {
    MessengerType.TELEGRAM: telegram_send_message,
    MessengerType.VK: vk_send_message,
}


@app.task()
def send_message_task(user_id: str, text, messenger):
    logger.info(f'abstaract sending to {user_id}')
    func = SOCIALS_MAPPING[messenger]
    async_to_sync(func)(user_id, text)
