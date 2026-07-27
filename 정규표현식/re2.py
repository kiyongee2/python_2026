
import re 

# 정규 표현식 패턴 컴파일
# match() 예시
pat = re.compile("[a-z]+")
match = pat.match("Hello World")
if match:
    print("매치된 문자열:", match.group()) #ello
    
# search() 예시
match = pat.search("Hello World")
if match:
    print("검색된 문자열:", match.group())
    
# '*' 은 0개 이상, '+'는 1개 이상
pat = re.compile("a*b")
match = pat.match("b")
if match:
    print("'*' 매치된 문자열:", match.group())

pat = re.compile("a+b")
match = pat.match("b")
if match:
    print("'+' 매치된 문자열:", match.group())
    
# fullmatch() 예시
pat = re.compile("[a-z]+")
match = pat.fullmatch("Hello")
if match:
    print("전체 매치된 문자열:", match.group())
else:
    print("전체 매치되지 않음")