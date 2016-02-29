import json
import time

data = []
filepath = './data/shooting_tweets/raw tweet data/tweets.json'
i = 0

#All the lines
toKeep = [u'contributors', u'truncated', u'text', u'is_quote_status', u'in_reply_to_status_id', u'id', u'favorite_count', u'source', u'retweeted', u'coordinates', u'entities', u'in_reply_to_screen_name', u'in_reply_to_user_id', u'retweet_count', u'id_str', u'favorited', u'retweeted_status', u'user', u'geo', u'in_reply_to_user_id_str', u'possibly_sensitive', u'lang', u'created_at', u'in_reply_to_status_id_str', u'place', u'extended_entities']

#Just the ones we're keeping
#For a complete list
#https://dev.twitter.com/overview/api/tweets
toKeep = ['coordinates', 'created_at', 'entities', 
	'favorite_count', 'geo', 'id_str', 
	'in_reply_to_screen_name', 'in_reply_to_status_id_str']

#Takes about 1.5 seconds per 100000 tweets without writing to file
#Takes about 1.6 seconds per 100000 tweets appending to file
start = time.time()
with open("testjson.json", "a") as cleanedTweets:
	with open(filepath) as f:
	    for line in f:
	    	i += 1
	    	jsonline = json.loads(line)
	    	jsonKeeping = {key: jsonline.get(key,None) for key in toKeep}
	    	
	    	cleanedTweets.write(json.dumps(jsonKeeping))
	        if (i % 10000 == 0):
	        	print i
	        	print time.time() - start
