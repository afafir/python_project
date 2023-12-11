from requests import Session

from config import settings
from schemas import Message


class MessageAPI:
    def __init__(self):
        self.session = Session()
        self.session.headers.update({
            'Authorization': 'Bearer ' + settings.BACK_API_TOKEN
        })

    def __enter__(self):
        self.session.__enter__()
        return self

    def __exit__(self, *args):
        self.session.__exit__()

    def send_message(self, message: Message):
        response = self.session.post(
            url=settings.MESSAGES_API_URL,
            json=message.dict(),
        )
        response.raise_for_status()
