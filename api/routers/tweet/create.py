import tweepy

from fastapi.responses import JSONResponse
from fastapi import status

from api.models.tweets import CreateTweet
from api.client.main import client


class CreateTweets:
    client: tweepy.Client = client

    @classmethod
    async def create(cls, data: CreateTweet):
        try:
            tweet = client.create_tweet(text=data.text)
        except Exception as e:
            return JSONResponse(
                content={"message": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return JSONResponse(
            {
                "message": "OK",
                "tweet_id": tweet.data['id']
            },
            status_code=status.HTTP_201_CREATED
        )
