import requests
from send_email import send_email

api_key = 'b02c08b3f9a44c378767ddefd5d87ddc'
url = f'https://newsapi.org/v2/everything?q=anime&from=2024-09-09&sortBy=publishedAt&apiKey={api_key}'

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ''

# Access the article titles and descriptions
for article in content['articles']:
    body = body + article['title']+'\n'+article['description']+'\n\n'
    
# message = ''.join(body)

message = body.encode('utf-8')
send_email(message=message)