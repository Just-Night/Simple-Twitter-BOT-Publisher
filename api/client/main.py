import tweepy

from config import config

# AUTH to API

client = tweepy.Client(
    bearer_token=config.TWITTER_BEARER_TOKEN,
    consumer_key=config.TWITTER_CONSUMER_KEY,
    consumer_secret=config.TWITTER_CONSUMER_SECRET,
    access_token=config.TWITTER_ACCESS_TOKEN,
    access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET
)
tweet_content = "Привіт, Twitter! Це мій перший твіт через Tweepy бота!"

# client.create_tweet(text=tweet_content)
