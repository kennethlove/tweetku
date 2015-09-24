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

def post():
    poem = Haiku()
    #twitter.statuses.update(status=poem)
    print(poem)

if __name__ == '__main__':
    if random.randint(3, 3) % 3 == 0:
        post()