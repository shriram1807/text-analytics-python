#Shriram Rangarajan
#MISM BIDA - Pyhton capstone
#Activity 2
#In this activity we strip of all html tags and display only the text content in the website
import urllib.request
from bs4 import BeautifulSoup
web_url = "http://www.opera.com/docs/changelogs/unified/2600/"
request_content = urllib.request.urlopen(web_url)
#store in soup object
soup = BeautifulSoup(request_content.read(),"lxml")
for content in soup(["script", "style"]):
    content.extract()

# get  the text content
content_text = soup.get_text()

#Splitting content into individual lines for removing trailing spaces
line_text = (line.strip() for line in content_text.splitlines())
#Merging all line content agian into one single text
parts = (phrase.strip() for line in line_text for phrase in line.split("  "))
# display in next lines dropping spaces
content_text = '\n'.join(parts for parts in parts if parts)
print(content_text)
