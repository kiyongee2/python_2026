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