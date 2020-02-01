import tweepy
import time
from authDetails import *


auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(access_key, access_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
tweets=[]


def single_post():
    try:
        tweet = str(input('Enter Tweet incl. hashtags '))
        api.update_status(tweet)
        print('successfully tweeted: ' + tweet)
    except tweepy.TweepError as e:
        print(e.reason)


def multi_tweets():
    i = 0
    seconds = 60
    tweets_amount = int(input('How many tweets would you like to queue '))
    min = int(input('In minutes how often would you like these tweets to be posted? '))
    while i < tweets_amount:
        tweet = input('Enter Tweet incl. hashtags ')
        tweets.append(tweet)
        i+=1
    for single_tweet in tweets:
        try:
            api.update_status(i)
            print('Tweeted '+ i)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        time.sleep(min * seconds)
