import json
import time
import os

data = []
baseFolderPath = './../data/shooting_tweets/raw tweet data/'
files = ['tweets.json', 'rest_tweets.json', 
	'rest_tweets2.json', 'rest_tweets3.json', 
	'rest_tweets4.json', 'rest_tweets5.json',
	'rest_tweets6.json', 'rest_tweets7.json',
	'rest_tweets8.json', 'rest_tweets9.json',
	'rest_tweets10.json', 'rest_tweets11.json',
	'rest_tweets12.json', 'rest_tweets13.json',
	'rest_tweets14.json', 'rest_tweets15.json',
	'rest_tweets16.json', 'rest_tweets17.json',
	'rest_tweets18.json',]
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
	'retweeted_status': {
		"id_str": 1,
	},
}

#Takes about 1.8 Seconds per 10000 json objects. 
start = time.time()
with open("./../cleanedShootingTweets.json", "a") as cleanedTweets:
	for tweetFile in files:
		filepath = os.path.abspath(baseFolderPath + tweetFile)
		with open(filepath) as f:
		    for line in f:
		    	i += 1
		    	jsonline = json.loads(line)
		    	newJson = {}
		    	for key in toKeep.keys():
		    		#This is not a nested hash
		    		if (toKeep[key] == 1):
		    			jsonVal = jsonline.get(key,None)
		    			newJson[key] = jsonVal
		    		#This is a nested hash
		    		else :
		    			jsonVal = jsonline.get(key,{})
		    			for key2 in toKeep[key].keys():
		    				if (toKeep[key][key2] == 1):
		    					subJson = jsonVal.get(key2, None)
		    					newKey = key + '_' + key2
				    			newJson[newKey] = subJson
				    		#handle user mentions separately because that's a list
				    		elif (key2 in ['user_mentions', 'hashtags']):
				    			subJson = jsonVal.get(key2, {})
				    			for key3 in toKeep[key][key2].keys():
									newKey = key + '_' + key2 + '_' + key3
									newJson[newKey] = []
									for j, jsonElem in enumerate(subJson):

				    				# print(jsonElem)
										newJson[newKey].append(jsonElem.get(key3,None))
						    			# print(newKey, newJson[newKey])

				    		#This is a twice-nested hash (we currently don't have 
				    		#this case, but it's here for completeness/in case we 
				    		#decide to add something)
				    		else :
				    			subJson = jsonVal.get(key2, {})
				    			for key3 in toKeep[key][key2].keys():
				    				newKey = key + '_' + key2 + '_' + key3
			    					subsubJson = subJson.get(key,None)
					    			newJson[newKey] = subsubJson.get(key3,None)
		    	# jsonKeeping = {key: jsonline.get(key,None) for key in toKeep}
		    	

		   #  	print newJson
		   #  	if (i > 5):
					# break	
		    	#Add a new line so we aren't just appending to the file. 
		    	cleanedTweets.write(json.dumps(newJson) + "\n")

					    
		        if (i % 100000 == 0):
		        	print "number of tweets parsed: ", i
		        	print "total time elapsed: ", time.time() - start
		print "finished file: ", tweetFile	



