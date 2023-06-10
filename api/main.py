"""
Main file of the api.
"""
import logging

from fastapi import FastAPI, APIRouter
from api.routers.health_check import router as health_check_router
from api.routers.tweet import router as tweet_router

app_routers = [
    tweet_router,
]

app = FastAPI(
    title="Twitter BOT Api",
    version="Development",
)

base_api_router = APIRouter(prefix="/api/v1")

for _router in app_routers:
    base_api_router.include_router(_router)
    logging.debug(f"Include {_router.prefix} to routers!")


app.include_router(base_api_router)
app.include_router(health_check_router)
