import json
import time
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

data = []
filename='./data/cleanedShootingTweets.json'
i = 0

#For now only want to read in a few lines of this file (about 100 tweets)
start = time.time()
with open(filename) as cleanedTweets:
    for tweet in cleanedTweets:
    	i += 1
    	if i > 3000 and i < 5000:
    		jsonline = json.loads(tweet)
    		data.append(jsonline)
    	elif i > 5000:
			break

df = pd.DataFrame(data=data)
df['DoW'] = df['created_at'].apply(lambda x: str(x)[0:3:])
df['Month'] = df['created_at'].apply(lambda x: str(x)[4:7:])
df['DoM'] = df['created_at'].apply(lambda x: str(x)[8:10:])
df['Hour'] = df['created_at'].apply(lambda x: int(str(x)[11:13:]))
df['Minute'] = df['created_at'].apply(lambda x: int(str(x)[14:16:]))
df['Minute'] = df['Minute'] + (df['Hour']-17)*60
df['HMS'] = df['created_at'].apply(lambda x: str(x)[11:19:])
# df.fillna(value=0,inplace=True)
# df.info()

# df['retweet_count'].value_counts(sort=True).plot(kind='bar')
# df['user_verified'].value_counts(sort=True).plot(kind='bar')
# df['user_followers_count'].value_counts(sort=True).plot(kind='bar')
# plt.scatter(df['user_followers_count'],df['retweeted'],c='g')
# df['user_time_zone'].value_counts(sort=True).plot(kind='bar')
# plt.scatter(df['Minute'],df['user_followers_count'])
df.plot(kind='scatter',x='Minute',y='user_followers_count')

plt.show()


