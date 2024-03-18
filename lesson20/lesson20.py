import urllib.request
import urllib
import re

print ("We will try to open this url, in order to get IP Address")

url ="http://checkip.dyndns.org"

print (url)

request = urllib.request.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print ("your IP Address is: ", theIP)