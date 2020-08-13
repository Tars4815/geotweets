"""
Created on Wed Aug 12 18:46:34 2020
@author: Tars4815
Filtering tweets by location and keyword using Tweepy library
"""
import tweepy
from tweepy import OAuthHandler
import json

#AUTHENTICATION STEP
#Insert here the auth parameters generated with Twitter developer account
consumer_key= "xxxxxx"
consumer_secret= "xxxxxx"
access_token="xxxxxx"
access_token_secret="xxxxxx"
#Finalize authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#ACTIVATE CURSOR WITH LOCATION, KEYWORD AND STARTING DATE
# public_tweets = tweepy.Cursor(api.search, count=100, q="hurricane -filter:retweets", geocode="25.761681,-80.191788,100km",since="2020-08-05",show_user = True,tweet_mode="extended").items() # Miami filtering
public_tweets = tweepy.Cursor(api.search, count=100, q="hurricane -filter:retweets", geocode="34.052235,-118.243683,1000km",since="2020-08-05",show_user = True,tweet_mode="extended").items() # Los Angeles filtering

#WRITING DATA IN A JSON FILE
for tweet in public_tweets:
    print(tweet.full_text)
    with open('ProvaCursoreLA1000km.json', 'a', encoding='utf8') as f:
        f.write(json.dumps(tweet._json))
        f.write("\n")
