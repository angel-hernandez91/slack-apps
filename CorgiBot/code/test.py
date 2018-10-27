from slackclient import SlackClient
#import os
slack_token = "xoxb-355147478502-oaGceWv4DWAXX8UZiCJ7MjbS"
sc = SlackClient(slack_token)
with open('C:\\Users\\angel.hernandez\\Desktop\\mmit_data_model_v2.xlsx') as file_content:
	sc.api_call("files.upload",channels="dev_self",file=file_content,title="Test upload")
