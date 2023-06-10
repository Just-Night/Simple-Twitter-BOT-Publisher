import uvicorn

from api import app
from config import API_HOST, API_PORT

# Start bot api
cfg = uvicorn.Config(app=app, host=API_HOST, port=API_PORT)
server = uvicorn.Server(cfg)
server.run()
