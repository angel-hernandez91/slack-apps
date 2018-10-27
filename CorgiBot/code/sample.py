import requests

url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'
response = requests.get(url).json()
try:
    quote_of_day = response[0]['content']
    # For formatting info, see https://api.slack.com/docs/message-formatting
    quote_of_day = quote_of_day.replace('&', '&amp;').replace('<p>', '').replace('</p>', '').replace('&amp;#8217;', "'")
    print(quote_of_day)
except:
    quote_of_day = "Some days are just bad days... That's all"