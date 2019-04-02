# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import time
from unidecode import unidecode

proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

quote_page = 'http://www.metrolyrics.com/taylor-swift-lyrics.html'
filename = 'lyrics_link'
# songs = pd.read_csv(filename)
with open('lyrics_link.csv') as f:
    lines = f.read().splitlines()

songs = {}
# for index, row in songs.iterrows():
for ind, song_url in enumerate(lines):
    page = urllib2.urlopen(song_url)
    soup = BeautifulSoup(page, 'html.parser')
    verses = soup.find_all('p', attrs={'class': 'verse'})

    lyrics = ''
    time.sleep(1)
    print ind

    for verse in verses:
        text = verse.text.strip()
        text = re.sub(r"\[.*\]\n", "", unidecode(text))
        if lyrics == '':
            lyrics = lyrics + text.replace('\n', '|-|')
        else:
            lyrics = lyrics + '|-|' + text.replace('\n', '|-|')



    songs[ind] = lyrics

    # print('saving {}'.format(row['song']))
    # songs.head()

print('writing to file')
with open('lyrics.json', 'a+') as fp:
    json.dump(songs, fp)
#songs.to_csv(filename, sep=',', encoding='utf-8')
