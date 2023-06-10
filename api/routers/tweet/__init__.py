from fastapi import APIRouter

from api.routers.tweet.create import CreateTweets

router = APIRouter(prefix='/tweets')

router.add_api_route('/create/', CreateTweets.create, methods=["POST"], status_code=201)
