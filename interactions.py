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

def search_user():
    search_phrase = str(input('What user would you like to search? '))
    temp_search = search_phrase
    for user in tweepy.Cursor(api.search, search_phrase).items():
        try:
            print(user)
            break
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    print('Would you like to see', temp_search,  'most recent tweets? ')
    see_more =str(input('Yes or No? '))
    if (see_more == "Yes" or'yes'):
        search_tweet(temp_search)


def search_tweet(search):
    tweet_amount = int(input('How many recent tweets would you like to see? '))
    for tweet in tweepy.Cursor(api.search,search).items(tweet_amount):
        try:
            print(tweet.text)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def follow_back():
    for follower in tweepy.Cursor(api.followers).items(1):
        try:
            follower.follow()
            print('Followed ', follower.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break