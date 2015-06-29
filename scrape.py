'''A simple script that tells us whether it is weekend yet'''

# import libraries
import urllib.request
from bs4 import BeautifulSoup

# open webpage
url = 'http://isitweekendyet.com/'
webpage = urllib.request.urlopen(url).read()

# turn html into beautiful soup
weekendSoup = BeautifulSoup (webpage)

# extract info from soup
ans = weekendSoup.body.div.string
# print to screen
print(ans)
# further processing?
if ans == 'YES':
	print('Get out and party')
else:
	print('Stay in')