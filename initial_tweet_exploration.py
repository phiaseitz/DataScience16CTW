import json
import time
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import cartopy.crs as ccrs

data = []
filename='./data/cleanedShootingTweets.json'
i = 0

#For now only want to read in a few lines of this file (about 100000 tweets)
start = time.time()
with open(filename) as cleanedTweets:
    for tweet in cleanedTweets:
    	i += 1
    	if i > 100000 and i < 300000:
    		jsonline = json.loads(tweet)
    		data.append(jsonline)
    	elif i > 300000:
    		break

df = pd.DataFrame(data=data)
df['retweet'] = df['text'].apply(lambda x: 'RT @' in x)
# df['DoW'] = df['created_at'].apply(lambda x: str(x)[0:3:])
# df['Month'] = df['created_at'].apply(lambda x: str(x)[4:7:])
# df['DoM'] = df['created_at'].apply(lambda x: str(x)[8:10:])
df['Hour'] = df['created_at'].apply(lambda x: int(str(x)[11:13:]))
df['Minute'] = df['created_at'].apply(lambda x: int(str(x)[14:16:]))
df['Minute'] = df['Minute'] + (df['Hour']-17)*60
# df['HMS'] = df['created_at'].apply(lambda x: str(x)[11:19:])

coords = []
for i in range(len(df)):
	location = df['coordinates'][i]
	try:
		coords.append(location.get('coordinates'))
	except:
		coords.append([0,0])

df['coords'] = coords
df['x'] = df['coords'].apply(lambda x: x[0])
df['y'] = df['coords'].apply(lambda x: x[1])

name = []
country = []
coordinates = []
full_name = []
for i in range(len(df)):
	location = df['place'][i]
	try:
		coordinates.append(location.get('bounding_box').get('coordinates'))
		name.append(location.get('name'))
		full_name.append(location.get('full_name'))
		country.append(location.get('country'))
	except:
		coordinates.append([[[0,0],[0,0],[0,0],[0,0]]])
		name.append('')
		full_name.append('')
		country.append('')

act_coords = []
for box in coordinates:
	actual_coord_x = (box[0][0][0]+box[0][1][0]+box[0][2][0]+box[0][3][0])/4
	actual_coord_y = (box[0][0][1]+box[0][1][1]+box[0][2][1]+box[0][3][1])/4
	act_coords.append([actual_coord_x,actual_coord_y])

df['city'] = name
df['country'] = country
df['full_name'] = full_name
df['coordinates'] = act_coords
df['x_p'] = df['coordinates'].apply(lambda x: x[0])
df['y_p'] = df['coordinates'].apply(lambda x: x[1])

ax = plt.axes(projection=ccrs.PlateCarree())
# shapename = 'admin_1_states_provinces_lakes_shp'
# states_shp = shpreader.natural_earth(resolution='110m',category='cultural', name=shapename)
ax.coastlines()
plt.scatter(df['x'],df['y'],color='r')
plt.scatter(df['x_p'],df['y_p'],color='g')
plt.show()


