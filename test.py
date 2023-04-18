from urllib.parse import urlparse
from html.parser import HTMLParser
import requests
from nltk.tokenize import word_tokenize
import bs4
from collections import Counter
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


##storing title
links=[]

##get the links for other pages


##indexing useful
data_list=[]

##queue for links
queue=[]


response=requests.get('https://www.google.com')
html_string=response.text



class Parser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag=='a':
            for attr in attrs:
                if attr[0]=='href':
                    print(attr[1])
                    links.append(attr[1])
                if attr[0]=='title':
                    data_list.append(attr[1])
        return super().handle_starttag(tag, attrs)
    
##cleaning up the crawler and using NLP to get the keywords
    
def test():
    response=requests.get('https://en.wikipedia.org/wiki/Earth')

    html=response.text

    soup=bs4.BeautifulSoup(html, "html.parser")
    text_content=soup.get_text()
    #print(text_content)

    stop_words=set(stopwords.words("english"))
    nltk.download('punkt')
    ps=PorterStemmer()
    tokens=word_tokenize(text_content.lower())
    #print(tokens)
    #print(stopwords)
    filtered_tokens=[]
    for token in tokens:
        if token not in stop_words and token.isalnum():
            filtered_tokens.append(token)
    
    words_common=Counter(filtered_tokens)

    #print(words_common)

    print(words_common.most_common(1))


    


    

test()


