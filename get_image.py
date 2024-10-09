import requests

url = 'https://upload.wikimedia.org/wikipedia/en/c/c5/Dragon_Ball_Z_Budokai_Tenkaichi.png?20210810141946'

response = requests.get(url)

with open('dbz.png','wb') as file:
    file.write(response.content)

