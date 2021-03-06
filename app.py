import tkinter as tk
from tkinter import *
from tweeting import *
from interactions import *
from reporting import *

def app():

    print('Thank you for using the Simple Twit Bot')
    print('Would you like to \n 1. Create tweet(s) \n 2. Search and Interactions \n 3. Reporting')
    choice = int(input('Numerical value beside option '))
    if choice ==1:
        tweet()
    elif choice == 2:
        search_interactions()
    elif choice == 3:
        reports()
    else:
        print('Invalid choice, please choose one of the options below')
        app()


def tweet():
    print('Would you like to \n 1. Tweet a single post \n 2. Tweet multiple posts \n 3. Tweet from CSV file')
    choice = int(input('Numerical value beside option '))
    if choice == 1:
        single_post()
    elif choice == 2:
        multi_tweets()
    elif choice == 3:
        tweet_csv()
    else:
        print('Invalid choice, please choose one of the options below')
        app()


def search_interactions():
    print('Would you like to \n 1. Search key word and like posts \n 2. Search for user')
    choice = int(input('Numerical value beside option '))
    if choice == 1:
        search_like()
    elif choice == 2:
        search_user()
    elif choice == 3:
        follow_back()
    else:
        print('Invalid choice, please choose one of the options below')
        app()


def reports():
    print('Would you like to \n 1. Search tweets \n 2. List followers \n 3. Most recent tweets retweeted')
    choice = int(input('Numerical value beside option '))
    if choice == 1:
        return_tweets()
    elif choice == 2:
        follower_count()
    elif choice == 3:
        recent_retweets()
    else:
        print('Invalid choice, please choose one of the options below')
        app()

while True:
    app()