from pydantic import BaseModel


class CreateTweet(BaseModel):
    text: str
