from django.conf import settings


class TelegramAPI:
    def __init__(self):
        from pyrogram import Client

        self.client = Client(
            "session",
            api_id=settings.TELEGRAM_API_ID,
            api_hash=settings.TELEGRAM_API_HASH,
            workdir=settings.BASE_DIR,
        )

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self.client.__aexit__(*args)

    async def send_message(self, user_id, text):
        if isinstance(user_id, str):
            if user_id.isdigit():
                user_id = int(user_id)
        await self.client.send_message(user_id, text)
