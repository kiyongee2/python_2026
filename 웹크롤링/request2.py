import requests

url = "https://www.python.org"
response = requests.get(url)

print(response)
print(response.status_code)
# print(response.text)

urls = ["https://www.python.org/", "https://www.naver.com/"]
filename = "robots.txt"

for url in urls:
  url_path = url + filename
  #https://www.python.org/robots.txt, https://www.naver.com/robots.txt
  print(url_path) 