
try:
  print('20' + 20)
except TypeError as e:
  print("자료형 오류가 발생했습니다:", e)
  # print('TypeError:', e)
  
try:
  print(10 / 0)
except ZeroDivisionError as e:
  print("0으로 나눌 수 없습니다:", e)
  # print('ZeroDivisionError:', e)
  
try:
  message = "Good Luck!" + friend
except NameError as e:
  print("변수가 정의되지 않았습니다:", e)
  # print('NameError:', e)
  
# 입력시 오류
'''
number = int(input("숫자를 입력하세요: "))
print(number + 10)
'''

try:
  number = int(input("숫자를 입력하세요: "))
  print(number + 10)
except ValueError as e:
  print("유효한 숫자를 입력하세요:", e)
  # print('ValueError:', e)
  
  