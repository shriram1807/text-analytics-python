#Shriram Rangarajan
#MISM BIDA - Pyhton capstone
#Activity 3
#In this activity , we strip the python html tags of the webpage and display its contents
#the text is then cleansed of punctuation marks and stopwords for further analysis

import urllib.request
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


web_url = "http://www.opera.com/docs/changelogs/unified/2600/"
request_content = urllib.request.urlopen(web_url)

#store in soup object
soup = BeautifulSoup(request_content.read(),"html.parser")
for content in soup(["script", "style"]):
    content.extract()

# get  the text content
content_text = soup.get_text()
print(content_text)



#  Removing punctuation
print('**********************************************************************************************')
punc_rem = set(string.punctuation)
new_text = ''.join(ch for ch in content_text if ch not in punc_rem)
new_text_list =[ch for ch in content_text if ch not in punc_rem]
print('Punctuation removed text --')
print(new_text)

# stop word removal
print('***********************************************************************************************')
stop_text = ' '.join([word for word in new_text.split() if word not in stopwords.words("english")])
stop_list = [word for word in new_text.split() if word not in stopwords.words("english")]
print(stop_text)


