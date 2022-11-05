rss = "https://news.google.com/?output=rss"
import re
import feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse(rss) #<<WORKS!!

#print[field for field in feed]

import pprint
#pprint.pprint(entry for entry in feed['entries'])
titles = [entry.title for entry in feed['entries']]

for title in titles:
    title_nosource=re.sub("\s\-\s.*","",title)
    title_source=re.sub(".*\s\-\s","",title)
    print title_source+" reports: "+title_nosource
    
entries = [entry for entry in feed['entries']]
#print entries


#.encode("utf-8")
