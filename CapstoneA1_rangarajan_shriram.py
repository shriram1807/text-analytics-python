#Shriram Rangarajan
#MISM BIDA - Pyhton capstone
#Activity 1
#This activity displays the html content of the webpage in the url
#Library used is Beautiful Soup
import urllib.request
from bs4 import BeautifulSoup
web_url = "http://www.opera.com/docs/changelogs/unified/2600/"
request_content = urllib.request.urlopen(web_url)
#store in soup object
soup = BeautifulSoup(request_content.read())
#print the content
print(soup.prettify())

