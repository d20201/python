'''A simple script that tells us whether it is weekend yet'''

# import libraries
import urllib.request
from bs4 import BeautifulSoup

# open webpage
url = 'http://bitcoinexchangerate.org/c/GBP/1'
webpage = urllib.request.urlopen(url).read()

# turn html into beautiful soup
bitSoup = BeautifulSoup (webpage)

# extract info from soup
print(len(bitSoup.body.div.h1))
# print to screen

# further processing?
