import os
import random

from twitter import *

from poems import Haiku

access_token = os.environ.get('twitter_access_token')
access_secret = os.environ.get('twitter_access_secret')
consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')

twitter = Twitter(
    auth=OAuth(
        access_token,
        access_secret,
        consumer_key,
        consumer_secret
    )
)

def post():  # pragma: no cover
    poem = Haiku()
    print(poem)
    """
    twitter.statuses.update(
        status=poem
    )
    """


if __name__ == '__main__':
    if not random.randint(3, 3) % 3:
        post()