from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re


tweets_data_path = "~/172/tweepy/twitter_data.txt"
	
tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue
