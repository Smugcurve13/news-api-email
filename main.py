import requests

api_key = 'b02c08b3f9a44c378767ddefd5d87ddc'
url = f'https://newsapi.org/v2/everything?q=anime&from=2024-09-09&sortBy=publishedAt&apiKey={api_key}'

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])