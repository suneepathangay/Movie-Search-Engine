from urllib.parse import urlparse
from html.parser import HTMLParser
import keyboard
import os
import re
import requests

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
        if tag=='a':
            for attr in attrs:
                if attr[0]=='href':
                    print(attr[1])
                    if attr[1] not in list_links:
                        list_links.append(attr[1])
                        queue.append(attr[1])
                if attr[0]=='title':
                    data_list.append(attr[1])
        return super().handle_starttag(tag, attrs)

    

parser=Parser()

def crawl():
    
        while(len(queue)!=0):
            try:
                if keyboard.is_pressed('q'):
                    break
                
                current_link=queue.pop()

                response=requests.get(current_link)
                parser.feed(response.text)
            except:
                print("eh")
                continue
        
        

crawl()





        




            






        



        #loop though and find the href or a tags for links
        ##add the link from each page to the queue
        ##pop from the queue and check if it is in visited url



    







