import json
import time

data = []
baseFolderPath = './data/shooting_tweets/raw tweet data/'
files = ['tweets.json', 'rest_tweets.json', 
	'rest_tweets2.json', 'rest_tweets3.json', 
	'rest_tweets4.json', 'rest_tweets5.json',
	'rest_tweets6.json', 'rest_tweets7.json',
	'rest_tweets8.json', 'rest_tweets9.json',
	'rest_tweets10.json', 'rest_tweets11.json',
	'rest_tweets12.json']
i = 0


#Just the ones we're keeping
#For a complete list
#https://dev.twitter.com/overview/api/tweets
toKeep = {
	'contributors': 1, 
	'text': 1, 
	'id_str': 1, 
	'is_quote_status': 1, 
	'in_reply_to_status_id_str': 1, 
	'favorite_count': 1, 
	'source': 1, 
	'retweeted': 1,
	'coordinates': 1, 
	'entities': {
		'hashtags': {
			'text': 1
		},
		'user_mentions': {
			'id_str': 1,
			'screen_name': 1,
		},
	},
	'retweet_count': 1,
	'in_reply_to_user_id_str': 1,
	'user': {
		'id_str': 1,
		'verified': 1,
		'followers_count': 1,
		'listed_count': 1,
		'is_translation_enabled': 1,
		'utc_offset': 1,
		'friends_count': 1,
		'location': 1,
		'geo_enabled': 1,
		'screen_name': 1,
		'lang': 1,
		'created_at': 1,
		'contributors_enabled': 1,
		'time_zone': 1,
	},
	'geo': 1,
	'possibly_sensitive': 1,
	'created_at': 1,
	'place': 1,
	}

#Takes about 1.8 Seconds per 10000 json objects. 
start = time.time()
with open("cleanedShootingTweets.json", "a") as cleanedTweets:
	for tweetFile in files:
		filepath = baseFolderPath + tweetFile
		with open(filepath) as f:
		    for line in f:
		    	i += 1
		    	jsonline = json.loads(line)
		    	newJson = {}
		    	for key in toKeep.keys():
		    		jsonVal = jsonline.get(key,None)
		    		#This is not a nested hash
		    		if (toKeep[key] == 1):
		    			newJson[key] = jsonVal
		    		#This is a nested hash
		    		else :
		    			for key2 in toKeep[key].keys():
		    				subJson = jsonVal.get(key2, {})
		    				if (toKeep[key][key2] == 1):
		    					newKey = key + '_' + key2
				    			newJson[newKey] = subJson
				    		#handle user mentions separately because that's a list
				    		elif (key2 in ['user_mentions', 'hashtags']):
				    			for j, jsonElem in enumerate(subJson):
				    				# print(jsonElem)
				    				for key3 in toKeep[key][key2]:
			    						newKey = key + '_' + key2 + '_' + str(j) + '_' + key3
				    					subsubJson = jsonElem.get(key,{})
						    			newJson[newKey] = subsubJson.get(key3,None)

				    		#This is a twice-nested hash (we currently don't have 
				    		#this case, but it's here for completeness/in case we 
				    		#decide to add something)
				    		else :
				    			for key3 in toKeep[key][key2].keys():
				    				newKey = key + '_' + key2 + '_' + key3
			    					subsubJson = subJson.get(key,None)
					    			newJson[newKey] = subsubJson.get(key3,None)
		    	# jsonKeeping = {key: jsonline.get(key,None) for key in toKeep}
		    	
		    	#Add a new line so we aren't just appending to the file. 
		    	cleanedTweets.write(json.dumps(newJson) + "\n")
		        if (i % 100000 == 0):
		        	print "number of tweets parsed: ", i
		        	print "total time elapsed: ",  time.time() - start
		print "finished file: ", tweetFile	



