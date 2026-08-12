# 리스트를 매개변수로 전달하는 함수 정의
def times(a):
  a2 = []
  for i in a:
    a2.append(i * 4)
  return a2

arr = [1, 2, 3, 4]
print(times(arr))

# 리스트를 매개변수로 전달하는 함수 정의
# 리스트의 합계를 계산하는 함수
def calc_sum(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

# 리스트의 평균을 계산하는 함수
def calc_avg(numbers):
    sum_val = calc_sum(numbers) #다른 함수를 호출
    return sum_val / len(numbers) # 평균 = 합계 / 개수

# 메인 영역 
num_list = [1, 2, 3, 4, 5]
print("리스트의 합:", calc_sum(num_list)) #함수 호출
print("리스트의 평균:", calc_avg(num_list))

# 리스트의 연산
x = [1, 2, 3]
y = [4, 5, 6, 10]

print(x) # [1, 2, 3]
print(y) # [4, 5, 6]
print(x + y) # [1, 2, 3, 4, 5, 6]
print(x * 2) # [1, 2, 3, 1, 2, 3]

# 리스트의 내포
squares = [x * x for x in range(1, 5)]
print(squares)

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

# 1부터 10까지 중 짝수만 저장
evens = []
for x in range(1, 11):
    if x % 2 == 0:
        evens.append(x)  
print(evens)