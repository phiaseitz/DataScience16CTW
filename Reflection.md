# Project Reflection

**Sophia and Victoria**

## Assessment Evidence and Interpretation
When we set out to do this project, our project goals were

*"Using data from the Twitter API, we would like to visualize how during political or social justice events information propogates through the Twitter network. In particular, we would like to look at: who is engaging, how many are engaging, how certain hashtags gain momentum (virality), and where conversations tend to happen on certain topics. Our minimum viable product will be a series of static visualizations of these questions with an intended reach goal of building an interactive visualizer. Overall, we want to inform people looking at our project on how information spreads, and perhaps discuss the implications of this knowledge."*

We feel that we have started to accomplish these goals, although we did not necessarily get as far as we would have liked. In an ideal world, our visualizations would have been interactive -- and potentially in the form of a web page rather than an Ipython notebook. That being said, we feel that we have produced some visualizations that help us understand with whom people were interacting on twitter, and have started to look into how users use hashtags to engage with certain causes. If you would like to see all of the visualizations that we created, please take a look at the notebooks in the `data_exploration` folder. These contain code for creating all the visualizations we made of the course of this project, including those that did not make it into our final writeup. 

## Changing the World
We believe that our product has potential to change the world, albeit with some UI changes. Understanding how social change/protest happens, or is organized, over social media is important; as more and more information about social justice happens over social media like twitter. 

Further, if we look at the recent political debates and how social justice groups like BlackLivesMatter are choosing to engage, there is a duality: present activism, and virtual activism. Present activism encapsulates the idea that a person is physically attending, acting, or rallying for a cause. Virtual activism is the shared support and shared knowledge for those causes online, often on social media platforms. The beauty of realtime social media sites like twitter, is the opportunity to unite these aspects of the social justice movement into a more powerful, impactful, and broader statement. Virtual activism serves as a way of organizing, sharing, and promoting causes. Communities can rally from across the world, and those that would otherwise not be exposed to certain movements now have that benefit.  

In balance, there is concern that virtual activism could replace present activism - the ease of retweeting trumps that of actually attending a rally. Of the millions of tweeters, how many were presently active? This is a hot topic within social justice circles, and an extension of our project easily lends itself to mapping, measuring, and starting a conversation about the dichotomy. Ideally, virtual activism will lead to present activism, and the study of motivations, communities, and networks could only lead to more insights about how to make this a reality. 

And with any social justice movement, the end goal is truly change for a community and thus for the world as people are asked to check their assumptions, and take a side. 

## Learning Goals
When we started out this project, we did not realize how large of a dataset we were dealing with. In other words, we might not have realized how ambitious our project really was. 

That being said, we learned a TON about how to handle large, text-based dataset. While this was not necessarily one of our learning goals, we feel that this is something that we really appreciated learning. This dataset forced us to make decisions about what functions to use, and how to process the dataset. For example, we learned about the relative speed differences between looping over all the rows in a dataframe, using the apply function, and using a pandas built-in function such as `to_datetime`. Had we not had such an unweildy dataset, we would not have learned about how to interact with a dataframe in a speedy matter. 

Additionally, we feel that, through a process of trial and error, we are starting to understand what kinds of visualizations are helpful for understanding twitter data and how users rally around a cause on twitter. Particularly relevant was a cursory exploration of node-graphs and node theory, which we started in the project, and think would be a great launching off point for someone to work on in the future.