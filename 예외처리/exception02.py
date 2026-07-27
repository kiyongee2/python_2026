
try:
  data = [20, 10, 30, 50]
  print(data[4])  
  print(data[3] / 0) 
except IndexError as e:
  print("리스트 인덱스 오류가 발생했습니다:", e)
except ZeroDivisionError as e:
  print("0으로 나눌 수 없습니다:", e)
  
# raise 키워드로 예외 발생시키기
def divide(a, b):
  if b == 0:
    raise ValueError("b는 0이 될 수 없습니다.")
  return a / b

try:
  result = divide(10, 0)
  print(result)
except ValueError as e:
  print("값 오류가 발생했습니다:", e)
  
