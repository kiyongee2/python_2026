import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.seoul.go.kr/main/index.jsp"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.select("a")

with open("seoul_links.csv", "w", newline="", encoding="utf-8-sig") as file:

    writer = csv.writer(file)

    # 제목 행
    writer.writerow(["메뉴명", "링크"])

    # 데이터 저장
    for link in links:

        text = link.get_text(strip=True)
        href = link.get("href")

        if text:
            writer.writerow([text, href])

print("CSV 저장 완료!")