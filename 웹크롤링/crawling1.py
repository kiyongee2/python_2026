import requests
from bs4 import BeautifulSoup

url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

