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


intitial_url='https://www.britannica.com/'


def crawl(url):
    
    #queue to store the links from each oage
        queue=[]
        queue.append(url)

        visited_links=[]
        visited_links.append(url)

        response=requests.get(url)

        

        

        
        


        #all the html in text format
        html=response.text

        #parser class to parse thorugh the HTML
        class Parser(HTMLParser):
            def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
                if tag=='a':
                    for attr in attrs:
                        if attr[0]=='href' and attr[1] not in visited_links:
                            queue.append(attr[1])
                            visited_links.append(attr[1])
                            #print(attr[1])

                return super().handle_starttag(tag, attrs)
        
        #creating parser instance
        parser=Parser()

        parser.feed(html)


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
            print(word_count.most_common(4))
            
        find_most_common_words(html)
            
        
        
        
        
        while len(queue)!=0:
                try:
                    current_link=queue.pop()
                    
                    crawl(current_link)
                except:
                    print("shit")
                    continue
        



crawl(intitial_url)

    













    







