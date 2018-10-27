from bs4 import BeautifulSoup
import json
import csv
import os

try:	
	import urllib.request as url_parse
	import urllib.parse as url_request

#setup for Python 2.7
except ImportError:
	import urllib as url_parse
	import urllib2 as url_request

outPath = os.getcwd() + '/' +  'imageURLs.csv'

def get_soup(url,header):
    return BeautifulSoup(url_parse.urlopen(url_parse.Request(url,headers=header)),'html.parser')


query = "corgi funny" # you can change the query for the image  here

image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)


header={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
soup = get_soup(url, header)

ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append(link)

with open(outPath, 'a') as image_url_list:
	wr = csv.writer(image_url_list)
	for url in ActualImages:
		wr.writerow([url])


print("there are total " + str(len(ActualImages)) +" images")