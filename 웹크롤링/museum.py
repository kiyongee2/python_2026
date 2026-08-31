import requests 
from bs4 import BeautifulSoup

# 1. 국립중앙박물관 > 관람정보 > 관람안내

# 2. url 가져오기
url = "https://www.museum.go.kr/MUSEUM/contents/M0101000000.do?menuId=tour-guidance"
response = requests.get(url)
# print(response.text)

# 3. BeautifulSoup, 첫번째 정보
html = BeautifulSoup(response.text, "html.parser")

first_url = html.select_one('ul.display-content')
print(first_url.get_text()) #관람 시간

# 4. 세부 목록
contents = html.select('ul.display-content-area > li > ul')
print(contents[1].get_text())

print("***** 관람 안내 *****")
for content in contents:
  print(content.get_text())

