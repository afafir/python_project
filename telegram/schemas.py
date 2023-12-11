from typing import Union

from pydantic import BaseModel


class MessageExtraData(BaseModel):
    user_id: Union[str, int]
    first_name: str
    last_name: str


class Message(BaseModel):
    text: str
    messenger: str
    extra_data: MessageExtraData
