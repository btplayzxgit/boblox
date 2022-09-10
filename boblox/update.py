import requests
from bs4 import BeautifulSoup

url = 'https://github.com/btplayzxgit/boblox'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')