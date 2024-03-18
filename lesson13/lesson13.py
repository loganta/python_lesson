#Importing the modules

import urllib.request
import json


screen_name = "wordpress"

url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + screen_name

data = json.load(urllib.request.urlopen(url))

print (len(data), "tweets")

for tweet in data:
	print(tweet['text'])