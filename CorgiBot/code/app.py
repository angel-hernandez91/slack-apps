#!/usr/bin/python
from flask import Flask, jsonify, request
import requests
import os
import glob
import random
import csv

application = Flask(__name__)

#need to load image URLs
imageURLs = open(os.getcwd() + '/' + 'imageURLs.csv')
csvReaderImg = csv.reader(imageURLs)


videoURLs = open(os.getcwd() + '/' + 'videoURLs.csv')
csvReaderVid = csv.reader(videoURLs)

corgiFacts = open(os.getcwd() + '/' + 'corgiFacts.txt')
csvReaderFacts = csv.reader(corgiFacts, delimiter='\t')

def csvToList(csvFile):
	URLList = []
	for item in csvFile:
		for i in range(0, len(item)):
			URLList.append(item[i])
	return URLList

imageURLList = csvToList(csvReaderImg)
videoURLList = csvToList(csvReaderVid)
corgiFactList = csvToList(csvReaderFacts)
#get random URL

def generateRandomLink(url_list):
	randomCorgi = random.randint(0, len(url_list)-1)
	url = url_list[randomCorgi]
	return url, randomCorgi

@application.route("/corgiquote", methods=["POST"], strict_slashes=False)
def returnQuote():
	url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
	response = requests.get(url).json()
	try:
		quote_of_day = response[0]['content']
		quote_of_day = quote_of_day.replace('<p>', '').replace('</p>', '').replace('&#8217;', "'").replace('&', '&amp;')
	except:
		quote_of_day = "Some days are just bad days... That's all"
	response = {"text": "Hello. I am CorgiBot. Here is your quote of the day!" ,"response_type": "in_channel","attachments": [{"text": quote_of_day}]}
	return jsonify(response)

@application.route("/corgiimage", methods=["POST"], strict_slashes=False)
def returnCorgiImage(): 
	image_url, urlNumber = generateRandomLink(imageURLList)
	response = {"text": "Here is the Corgi you requested. Please enjoy!", "response_type": "in_channel", "attachments": [{"image_url": image_url}]}
	return jsonify(response)

@application.route("/corgivideo", methods=["POST"], strict_slashes=False)
def reutrnCorgiVideo():
	video_url, urlNumber = generateRandomLink(videoURLList)
	response = {"text": "Here is the Corgi Video you requested \n" + video_url, "response_type": "in_channel" }
	return jsonify(response)

@application.route("/corgifact", methods=["POST"], strict_slashes=False)
def returnCorgiFact():
	fact, factNumber = generateRandomLink(corgiFactList)
	response = {"text": "Corgi Fact #" + str(factNumber), "response_type": "in_channel", "attachments": [{"text": fact}]}
	return jsonify(response)

if __name__ == "__main__":
	application.run(host='0.0.0.0',port=4000)
