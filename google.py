#! /usr/bin/env python3
# google.py opens several google search results in subsequent tabs

import requests, sys, webbrowser, bs4

def main():

	print('Googling.....') # display test while googling 
	res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
	res.raise_for_status()

	# Retrieve top search results links
	soup = bs4.BeautifulSoup(res.text, "html.parser")

	# Open a browser tab for each result
	linkElems = soup.select('.r a')
	numOpen = min(5, len(linkElems))
	for i in range(numOpen):
		print(linkElems[i].get('href'))
		webbrowser.open('http://google.com' + linkElems[i].get('href'), new = 2)





if __name__ == '__main__':
	main()