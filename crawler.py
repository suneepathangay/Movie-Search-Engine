from urllib.parse import urlparse
from html.parser import HTMLParser
import keyboard
import sqlite3
from nltk.tokenize import word_tokenize
import os
import re
import bs4
import requests
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import threading
import sqlite3




def find_most_common_words(html):
            soup=bs4.BeautifulSoup(html,'html.parser')
            text_content=soup.get_text()
            stop_words=set(stopwords.words("english"))
            tokens=word_tokenize(text_content.lower())
            filtered_tokens=[]
            
            for token in tokens:
                if token not in stop_words and token.isalnum():
                        filtered_tokens.append(token)

            word_count=Counter(filtered_tokens)
            return word_count.most_common(5)



def extract_link(link):
    url=""
    link=link.replace('/url?q=','')
    for chars in link:
        if chars=='&':
            break
        else:
            url=url+chars
    return url

list_links=[]
seed='https://myflixer.to/movie'
list_links.append(seed)

base_link='https://myflixer.to'

visisted_links=set()

class Parser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag=='a':
            
            for attr in attrs:
                if attr[0]=='href':
                        result = re.split(r'[/\?]', str(attr[1]))
                    
                        if len(result)>=3:
                            if result[1]=="movie":
                                link=base_link+attr[1]
                                print(link)
                                list_links.append(link)
                        
                            
        
parser=Parser()


# res=requests.get(list_links.pop(0))

# parser.feed(res.text)

while len(list_links)!=0:
    try:
        link=list_links.pop(0)
        if link not in visisted_links:
            res=requests.get(link)
            parser.feed(res.text)
            visisted_links.add(link)
        else:
            continue
    except:
        continue















