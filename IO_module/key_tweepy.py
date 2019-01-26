#! /usr/bin/python
#
#   key_tweepy.py
#
#                      
# ------------------------------------------------------------------
import  tweepy

def key_tweepy_proc():
    consumer_key=''
    consumer_secret=''
    access_token_key=''
    access_token_secret=''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    return api
#
# ------------------------------------------------------------------
