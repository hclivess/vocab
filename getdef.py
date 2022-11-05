import os
import re
import requests
import time
from HTMLParser import HTMLParser
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
# set header
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
# set header
lines = [line.rstrip('\n') for line in open('dict_desc.txt')]
for line in lines:
    try:
        print line
        request = requests.get("https://en.wiktionary.org/wiki/"+line, headers=hdr)
        geturl_readable = request.text
        stripped = strip_tags(geturl_readable)
        word = re.findall("Pronunciation[\s\S]+?\n\n\n\n", stripped)
        
        if word == []:
            word = re.findall("Etymology[\s\S]+?\n\n\n\n", stripped)
            #print word
        if word == []:
            word = re.findall("Noun[\s\S]+?\n\n\n\n", stripped)
            #print word
        if word == []:
            word = re.findall("[\s\S]+{300}", stripped)

        print word
            
        word = word[-1].encode("utf-8")
        word = word.replace("[edit]","")
        word = word.replace("\n\n\n\n","")
        word = word.decode("utf-8")
        line = line.title()
        f = open("output\\"+line+".txt","w") 
        f.write(word.encode("utf-8")) 
        f.close() 
        link = re.findall ('\"canonical\" href\=\"(.*)', geturl_readable)
        link = link[0].encode("utf-8")
        
    except:
    
        try:
          word = "Word definition not found, please try searching Google for more information"
          line = line.title()
          f = open("output\\"+line.lower()+".txt","w") 
          f.write(word.encode("utf-8")) 
          f.close() 
          link = re.findall ('\"canonical\" href\=\"(.*)', geturl_readable)
          link = link[0].encode("utf-8")
        except:
          pass
#print link.decode("utf-8")        
