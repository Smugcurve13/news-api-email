import requests

api_key = 'b02c08b3f9a44c378767ddefd5d87ddc'
url = f'https://newsapi.org/v2/everything?q=nvidia&from=2024-09-09&sortBy=publishedAt&apiKey={api_key}'

request = requests.get(url)
content = request.text
print(content)