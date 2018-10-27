
from google_images_download import google_images_download   #importing the library
import argparse

#arguments
argsparser = argparse.ArgumentParser()
argsparser.add_argument("keywords")
argsparser.add_argument("limit")
args = argsparser.parse_args()

keywords = args.keywords
limit = args.limit

response = google_images_download.googleimagesdownload()   #class instantiation


def getImages(keywords, limit):
	arguments = {"keywords":keywords,"limit":limit,"print_urls":True}   #creating list of arguments
	return response.download(arguments) 

getImages(keywords, limit)