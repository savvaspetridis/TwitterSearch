'''
twitter_search written by Savvas Petridis
March 7, 2015
'''

import requests
import oauth2 as oauth
import json
import sys
import random
from urllib import quote

CONSUMER_KEY = 'VU3JTWuHigpWeq5Kka4s8JnVX'
CONSUMER_SECRET = 'G6ypBQ1ZCsDb6p2MpBo5sY2W0w4BofhcTqIpE61DZT3wO5e5Z1'
ACCESS_KEY = '706792626188582912-JPkLRQ37BFAjxyZgnp215kjeJMg7aeT'
ACCESS_SECRET = '2yq7CmyVZj20dmeC36P94C2H7dQSR0ysIK64SJgOW2L6n'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

# searchs for a tweet in the twitter API containing a certain keyword
# prints a random tweet from the search
def search(keyword):
	# format url & encode special characters in the keyword
	url_encode_keyword = "\"" + quote(keyword) + "\""
	search_url = 'https://api.twitter.com/1.1/search/tweets.json?&q=' + url_encode_keyword

	# connect & get data from API
	response, data = client.request(search_url)
	tweets = json.loads(data)
	statuses = tweets['statuses']

	# get random tweet 
	tweet = get_random_tweet(keyword, statuses)

	print_tweet_info(tweet, keyword)


# scans for links/media in the tweet & returns string detailing them
def media_scan(tweet):
	media_description = ""
	for url in tweet['urls']: 
		# concatenates string "media_description" which details all the media in the post
		media_description = media_description + url['expanded_url'] + ", "
	# add links to media that are in the tweet's content
	if "media" in tweet:
		for media_link in tweet['media']:
			media_description = media_description + media_link['media_url_https']
	return media_description


# returns random tweet containing the keyword in its content
def get_random_tweet(keyword, statuses):
	tweet_exists = False
	# keeps track of tweets (which contain the keyword) from 'statuses'
	tweet_positions = []
	tweet_i = 0
	for tweet in statuses:
		tweet_content = tweet['text']
		if keyword.lower() in tweet_content.lower():
			tweet_exists = True
			# add tweet at position 'tweet_i' in 'statuses' to 'tweet_position list'
			tweet_positions.append(tweet_i)
		tweet_i = tweet_i + 1

	if(tweet_exists):
		tweet_number = len(tweet_positions)
		# get random number from 0 to (tweet_number - 1)
		random_i = int (random.random() * tweet_number)
		# return random tweet
		return statuses[tweet_positions[random_i]]
	else:
		return None


def print_tweet_info(tweet, keyword):
	if tweet == None:
		print "No tweet with keyword: \"" + keyword + "\""
	else:
		# create string detailing all the media
		media_text = media_scan(tweet['entities'])
		# print "@username: tweet that contains <keyword>"
		print("@" + tweet['user']['screen_name'] + ": " + tweet['text'])
		# print media string
		print("media: " + media_text)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("twitter_search.py <keyword>")
		sys.exit()
	search(sys.argv[1])