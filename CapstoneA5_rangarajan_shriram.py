#Shriram Rangarajan
#MISM BIDA - Pyhton capstone
#Activity 5
#In this activity , we strip the python html tags of the webpage and display its contents
#the text is then cleansed of punctuation marks and stopwords for further cleansed
#the words in the final corpus are dispalyed in the order of their frequencies

import urllib.request
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

from collections import Counter, defaultdict

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


# stop word removal
print('***********************************************************************************************')
stop_text = ' '.join([word for word in new_text.split() if word not in stopwords.words("english")])
stop_list = [word for word in new_text.split() if word not in stopwords.words("english")]


# frequency of occurrence and values are lists the words encountered
rep_word = defaultdict(list)
for word, freq in Counter(stop_list).items():
  rep_word[freq].append(word)

# print in order of occurrence (with sorted list of words)
print("Words in the order of their occurences :")
for freq in sorted(rep_word):
  print('Occurence {} times: {}'.format(freq, sorted(rep_word[freq])))

