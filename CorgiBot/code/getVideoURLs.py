from bs4 import BeautifulSoup
import json
import csv
import os
import requests

try:	
	import urllib.request as url_parse
	import urllib.parse as url_request

#setup for Python 2.7
except ImportError:
	import urllib as url_parse
	import urllib2 as url_request

url = 'http://www.youtube.com'

sb_get = requests.get(url)
sb_get.content

header={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}

requests.get(url, headers=header)

search_url = "/results?search_query="
search_term = "corgi"

search_term = search_term.split()
search_term ='+'.join(search_term)

sb_url = url + search_url + search_term

sb_get = requests.get(sb_url, headers=header)

sb_get.content

soup = BeautifulSoup(sb_get.content, "html.parser")

ytLinks = soup.findAll('a', class_='yt-uix-tile-link')

ytList = []
for link in ytLinks:
	yt_href = link.get("href")
	finalURL = url + yt_href
	ytList.append(finalURL)

outPath = os.getcwd() + '/' +  'videoURLs.csv'

with open(outPath, 'a') as video_url_list:
	wr = csv.writer(video_url_list)
	for url in ytList:
		if "/user/" not in url:
			wr.writerow([url])

