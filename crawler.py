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


##we need to change the starting url. It sucks
initial_url='https://en.wikipedia.org/wiki/Earth'




queue=[]
queue.append(initial_url)

##storing links
list_links=[]

##get the links for other pages
data_list=[]

##class to create the HTML parser and go thouhg the tags
class Parser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        #going to the other links
        if tag=='a':
            for attr in attrs:
                if attr[0]=='href' and attr[1] not in list_links:
                    #print(attr[1])
                    #with open('links.txt','a') as f:
                       # f.write(attr[1]+"\n")
                        #f.close()
                    if attr[1] not in list_links:
                        list_links.append(attr[1])
                        queue.append(attr[1])
        return super().handle_starttag(tag, attrs)

    

parser=Parser()

def crawl():
    
        while(len(queue)!=0):
            
            try:
                
                current_link=queue.pop()

                response=requests.get(current_link)

                soup=bs4.BeautifulSoup(response.text, "html.parser")
                text_content=soup.get_text()
                stop_words=set(stopwords.words("english"))
                tokens=word_tokenize(text_content.lower())
                filtered_tokens=[]
                for token in tokens:
                    if token not in stop_words and token.isalnum():
                        filtered_tokens.append(token)
    
                words_common=Counter(filtered_tokens)

    #print(words_common)

                print(words_common.most_common(3))
                

                parser.feed(response.text)



            except:
                print("eh")
                continue
        
        

crawl()







        




            






        



        #loop though and find the href or a tags for links
        ##add the link from each page to the queue
        ##pop from the queue and check if it is in visited url



    







