import urllib.request
import re

url = "https://magestore.zendesk.com/hc/en-us"
#connect to a URL
website = urllib.request.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall("(http|ftp)s?://.*?)",html)

print (links)