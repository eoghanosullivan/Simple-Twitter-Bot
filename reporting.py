import tweepy
import time
from authDetails import *

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(access_key, access_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


def return_tweets():
    amount = int(input('How many tweets would you like to report on '))
    for tweet in tweepy.Cursor(api.user_timeline).items(amount):
        print('Amount of likes ', tweet.favorite_count, '\nTweet: ', tweet.text, '\nRetweet(s) ', tweet.retweet_count)
        time.sleep(10)


def follower_count():
    follower_list = []

    for follower in tweepy.Cursor(api.followers).items():
        follower_list.append(follower)
    print('You have a total of ', len(follower_list), 'followers')

def recent_retweets():
    limit = int(input('How many tweets would you like to check'))
    for retweet in tweepy.Cursor(api.retweets_of_me).items(limit):
        print(retweet.text, ' was retweeted originally on ',retweet.created_at, ' ', retweet.retweet_count, ' time(s)')
