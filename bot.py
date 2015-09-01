import random

from twitter import *

from poems import Haiku

twitter = Twitter(
    auth=OAuth(
        "3331240092-1qKSOSLccsvU7wdwKqzrGH7MOHEXfZCrb9O0mOh",
        "Pp8pLlaEYp0Nj6ybwLVN6mDXjsXC2xtGVoPZtivCtiGLM",
        "5KQSckXJITX5e0USoRcxK7gjG",
        "trClWvx6mC9ihGj4FXxaVHPuyWrhXekszDlqpJAj3EKT17BNHa",
    )
)

def post():
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