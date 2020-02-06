import tweepy
import time
import csv
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

def tweet_csv():
    tweets=[]
    with open('tweet_list_test.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for new_tweet in csv_reader:
            tweets.append(new_tweet)
            print(*new_tweet)
        for tweet in tweets:
            try:
                api.update_status(*tweet)
                print('successfully tweeted: ', *tweet)
                time.sleep(10)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break