from pyrogram import Client

app = Client("session")


async def parse():
    async with app:
        ...
