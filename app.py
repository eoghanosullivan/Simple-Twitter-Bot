from tweeting import *
from interactions import *


def app():
    print('Thank you for using the Simple Twit Bot')
    print('Would you like to \n 1. Create tweet(s) \n 2. Search and Interactions')
    choice = int(input('Numerical value beside option '))
    if choice ==1:
        tweet()
    elif choice == 2:
        search_interactions()
    else:
        print('Invalid choice, please choose one of the options below')
        app()


def tweet():
    print('Would you like to \n 1. Tweet a single post \n 2. Tweet multiple posts')
    choice = int(input('Numerical value beside option '))
    if choice == 1:
        single_post()
    elif choice == 2:
        multi_tweets()
    else:
        print('Invalid choice, please choose one of the options below')
        app()


def search_interactions():
    print('Would you like to \n 1. Search jey word and like posts')
    choice = int(input('Numerical value beside option '))
    if choice == 1:
        search_like()
    else:
        print('Invalid choice, please choose one of the options below')
        app()

app()
