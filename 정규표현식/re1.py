
import re

text = "내 전화번호는 010-1234-5678입니다."
pattern = r"\d{3}-\d{4}-\d{4}"
match = re.search(pattern, text)
if match:
    print("전화번호:", match.group())
    
email_text = "제 이메일 주소는 sudo2100@naver.com입니다."
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_match = re.search(email_pattern, email_text)
if email_match:
    print("이메일 주소:", email_match.group())
    
url_text = "제 웹사이트는 https://www.example.com입니다."
url_pattern = r"https?://[^\s]+"
url_match = re.search(url_pattern, url_text)
if url_match:
    print("웹사이트 URL:", url_match.group())
    
# findall 예시
text = "오늘은 2024-06-01입니다. 내일은 2024-06-02입니다."
date_pattern = r"\d{4}-\d{2}-\d{2}"

dates = re.findall(date_pattern, text)
print("날짜 목록:", dates)

text = "사과 3개, 배 5개, 오렌지 2개"
fruit_pattern = r"\d+"
fruit_counts = re.findall(fruit_pattern, text)
print("과일 개수 목록:", fruit_counts)

# sub 예시
text = "내 전화번호는 010-1234-5678입니다."
masked_text = re.sub(pattern, "XXX-XXXX-XXXX", text)
print("마스킹된 텍스트:", masked_text)
