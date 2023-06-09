from urllib.parse import urlparse
from html.parser import HTMLParser


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
import db
from embedding import text_to_vector



def crawl():

    base_link='https://myflixer.to'

    class Parser(HTMLParser):
        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag=='a':
                for attr in attrs:
                    if attr[0]=='href':
                            result = re.split(r'[/\?]', str(attr[1]))
                            if len(result)>=3:
                                if result[1]=="movie":
                                    link=base_link+attr[1]
                                    db.post_data(link)
                                    print(link)
    parser=Parser()                          


    for number in range(654,1230):
        print(number)
        link=f'https://myflixer.to/movie?page={number}'
        rees=requests.get(link)
        parser.feed(rees.text)



crawl()
