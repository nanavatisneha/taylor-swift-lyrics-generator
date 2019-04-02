import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
from unidecode import unidecode

proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

quote_page = urllib2.urlopen("http://www.metrolyrics.com/taylor-swift-lyrics.html")
soup = BeautifulSoup(quote_page, "lxml")
links = []
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(links)
