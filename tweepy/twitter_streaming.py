#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re

#Variables that contains the user credentials to access Twitter API 
access_token = "2358696205-bEUbsHFv5pwpmw8JS0oOqCEMD8lGSyxXD6jELHN"
access_token_secret = "tLyFwTK4iFgXYLpq8COjE71n3AjhjtuEirX4kdaEnr6Yp"
consumer_key = "9zfJNe39F7R6isb9qtr8PkGQ4"
consumer_secret = "2q4BJdK0khZV8xIrjPyqtqYs0AtEQUecVE8DTZXMy30ZJiIoDv"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
		def on_data(self,data):
				parsed_json = json.loads(data)
				txt = parsed_json['text']
				print(parsed_json['entities'])
				#url = parsed_json['entities'][urls]
				username = parsed_json['user']['screen_name']
				tweet = "User:" + username + ":" + txt + "Url:"+ "\n"
				print(tweet)
				return True

		def on_error(self,status):
				print status

if __name__ =='__main__':
 #This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth,l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(locations=[-122.75,36.8,-121.75,37.8])


	#tweets_data_path = "~/172/tweepy/twitter_data.txt"
	
#	tweets_data = []
#	tweets_file = open(tweets_data_path,"r")
#	for line in data:
#		try:
#				tweet = json.loads(line)
#				tweets_data.append(tweet)
#				print tweet
#		except:
#				continue
