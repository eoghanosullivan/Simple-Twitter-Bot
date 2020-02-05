import tweepy
import time
from authDetails import *


auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(access_key, access_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def search_like():
    search_phrase = str(input('What key word would you like to search? '))
    search_amount = int(input('How many posts would you like to search for? '))

    for tweet in tweepy.Cursor(api.search, search_phrase).items(search_amount):
        try:
            tweet.favorite()
            print('Tweet liked @', tweet.user.screen_name, ': ', tweet.text)
            time.sleep(200)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

