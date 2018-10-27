import urllib
from PIL import Image
import os
import glob
import random
import argparse
# from google_images_download import google_images_download   #importing the library

# response = google_images_download.googleimagesdownload()   #class instantiation

# arguments = {"keywords":"Corgi,Meme,Funny","limit":1,"print_urls":True}   #creating list of arguments
# response.download(arguments) 
argsparser = argparse.ArgumentParser()
argsparser.add_argument("message")
argsparser.add_argument("image_type")
args = argsparser.parse_args()

message = args.message
image_type = args.image_type

currDir = os.getcwd()


filepath = currDir + '\\' + 'downloads'
filenames = []
for root, dirs, files in os.walk(filepath):
    for directory in dirs:
        if directory == image_type:
            curr_src = glob.glob(os.path.join(root, directory, '*'))
        for src in curr_src:
                filenames.append(src)

randCorgi = random.randint(0, len(filenames) -1)

jpgPath = str(filenames[randCorgi])
#jpgfile = Image.open(jpgPath)

#setup for Python 3+
try:	
	import urllib.request as url_parse
	import urllib.parse as url_request

#setup for Python 2.7
except ImportError:
	import urllib as url_parse
	import urllib2 as url_request
#jpgPath = 'C:\\Users\\angel.hernandez\\Desktop\\mmit_data_model_v2.xlsx'
#method to post a message to a channel as a user
def slackPost(message, channel, username, method_type):
    message_encoded = url_request.urlencode({'text':message})
    channel_encoded = url_request.urlencode({'channel':channel})
    username_encoded = url_request.urlencode({'as_user':'false','username':username})
    token_encoded = url_request.urlencode({'token':API_TOKEN})

    if method_type == 'chat':
        method = 'chat.postMessage'
       
        full_post_path = method + '?' + message_encoded + '&' + channel_encoded + '&' + username_encoded + '&' + token_encoded
        response = url_parse.urlopen(SLACK_API_ROOT + full_post_path)
        return response
    else:
        method = 'files.upload'
        post = 'curl -F file=@"' + str(jpgPath) + '" -F initial_comment="' + message + '" -F channels=' + channel + ' -F token=' + corgi_token + ' ' + SLACK_API_ROOT + method
        print(post)
        response = os.system(post)
        return response


print('Posting')
slackPost(message, 'dev_self', 'SlackBot', 'file')
