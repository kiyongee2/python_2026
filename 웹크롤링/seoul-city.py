import requests
from bs4 import BeautifulSoup

# 1단계. HTML 구조 확인하기
'''브라우저에서 서울시청 홈페이지를 열고:
F12 → Elements(요소) 를 선택합니다.
공공서비스예약, 서울소식, 주요뉴스 같은 글자를 찾아보세요.
CSS 선택자 확인'''


# 2단계. requests로 서울시청 HTML 가져오기
url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)
# print(response.text)

# 3단계. BeautifulSoup으로 HTML 분석하기
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) #title 태그
print(soup.title.text) # 제목 문자열

# 4단계. 모든 링크 가져오기
links = soup.select("a")

for link in links:
    text = link.get_text(strip=True)

    if text:
        print(text)
        
# 5단계. 링크 주소까지 가져오기
for link in links:
    text = link.get_text(strip=True)
    href = link.get("href")

    if text:
        print(text, "→", href)