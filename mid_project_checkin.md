# Mid Project Checkin
### By Sophia and Victoria

## Goals
Our goals for this mid-project checkin were to 
* Have Data
* Have an understanding of what information the dataset contains and how to access that information
* Have plans for our final visualizations and preliminary visualizations. 

We believe that we have accomplised these goals, although the documentation for code produced in accomplishing these goals is not entirely to our standard. 

## Accomplishments Thus Far
Thus far, we have:
* Found a sustainable method of downloading tweets, using twarc.py [documentation](https://github.com/edsu/twarc). This library allows us to query the twitter API and download tweets from a list of tweets ids. 

* We have looked through the tweets, and the twitter API [documentation](https://dev.twitter.com/rest/reference/get/statuses/lookup) as well as the [documentation on tweet objects](https://dev.twitter.com/overview/api/tweets) to decide what information in each tweet that we want to keep. Most fields of interest like retweet/friend count are populated. On the otherhand, fields contanint location data are the least likely to be populated. We have chosen to keep approximately half of the indicators given to us by the twitter API. 

* We have created a cleaning function that, given a file of raw tweet data, cleans the tweets, keeping only the information we want and flattening the json, so that there is no nested json. This code van be found in the development_scripts/clean_json_data.py. 

* We have started exploring the data and created preliminary plots of our data. These plots include a visualization of how the most popular hashtags over time and a location-based visualization of the tweets that occurred. These explorations can be found in Most_Popular_Hashtags.ipynb and Spatial_Representations.ipynb. 

* We have also started to plan out our final visualization(s).
	* Our minumum viable product product will be a map-based, temporal visualization of the number of tweets mentioning Ferguson over time. We are planning on producing similar visualizations for both the tweets related to the shooting and the tweets shortly after the (lack of) indictment. 
	* Additionally, a stretch goal would be a visualization depicting how the most re-tweeted tweets spread over time, or how a tweet goes viral over time.
	* Another thing that we are interested in investigating if the time allows is when celebrities and/or public organizations (verified twitter accounts) get involved -- how do celebrities/public figures play a role in the conversation about Ferguson over social media. git

