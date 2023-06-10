import os

# INTERNAL Api settings
API_HOST = os.environ.get('API_HOST', 'localhost')
API_PORT = int(os.environ.get('API_PORT', '8080'))
API_LOG_LEVEL = os.environ.get('API_LOG_LEVEL', 'INFO')


# BOT settings
TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN', None)
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', None)
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', None)
