import requests
from send_email import send_email

topic = 'india'

api_key = 'b02c08b3f9a44c378767ddefd5d87ddc'
url = 'https://newsapi.org/v2/everything?'\
f'q={topic}&'\
'from=2024-09-09&'\
'sortBy=publishedAt&'\
f'apiKey={api_key}&'\
'language=en'

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
subject = "subject: Today's Samachar \n"
body = ''

# Access the article titles and descriptions
for article in content['articles'][:20]:
    body += subject
    if article['title'] is not None:
        body = body + article['title']+'\n'\
        + article['description']+'\n' +\
        article['url']+'\n\n'\
    
# message = subject + body

message = body.encode('utf-8')
send_email(message=message) 