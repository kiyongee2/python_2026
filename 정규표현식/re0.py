import re

# match() : 문자열의 "처음"부터 패턴이 맞는지
m = re.match('[a-z]+', 'korea')
print(m.group()) 

# search() : 문자열 "어디든" 패턴이 있으면 반환
s = re.search('\d+', 'abc123def')
print(s.group()) 

# findall() : 패턴에 맞는 "모든" 값을 리스트로
nums = re.findall('\d+', 'a1 b22 c333')
print(nums) 

# sub() : 패턴을 찾아 다른 문자열로 치환
print(re.sub('\d', '*', 'a1b2c3'))   # a*b*c*