from bs4 import BeautifulSoup
try:	
	import urllib.request as url_parse
	import urllib.parse as url_request

#setup for Python 2.7
except ImportError:
	import urllib as url_parse
	import urllib2 as url_request

import re
#------------
page = 'http://glados.serveftp.com/corgi_images'
html_page = url_parse.urlopen(page)
soup = BeautifulSoup(html_page, 'lxml')


image_links = []



for link in range(5, len(soup.findAll('a'))-1):
	image_links.append(soup.findAll('a')[link].get('href'))

print(image_links)
