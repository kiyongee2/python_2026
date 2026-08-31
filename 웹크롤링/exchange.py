import requests
from bs4 import BeautifulSoup

# 1. 네이버 > 증권 > 시장지표 

# 2. url
url = "https://finance.naver.com/marketindex/"
response = requests.get(url)

# 3. html parsing
soup = BeautifulSoup(response.text, 'html.parser')

# 4. 환율 정보 - 첫째 항목
exchange_name = soup.select_one('ul.data_lst span.blind').text 
print(exchange_name) #미국 USD
exchange_price = soup.select_one('ul.data_lst span.value').text 
print(exchange_price)

# 5. 환율 정보 - 모든 항목
all_li = soup.select('div.market1 ul li')
# print(all_li)

for li in all_li:
  exchange_name = li.select_one('span.blind').get_text()
  exchange_price = li.select_one('span.value').get_text()
  # print(f"{exchange_name} : {exchange_price}")
  print(f"{exchange_name.split()[1]} : {exchange_price}")





  