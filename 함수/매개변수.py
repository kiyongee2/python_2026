
# 매개변수 - 함수의 괄호안에 포함되는 변수이다.
# 기본 매개변수(default parameter)

def take_bus(fare=1500):
    print(f"버스 요금은 {fare}원입니다.")
    
take_bus() #버스 요금은 1500원입니다.
take_bus(1700) #버스 요금은 1700원입니다.

# 가변 매개 변수
def calc_average(*numbers):
    # total = sum(numbers) # 내장 함수 sum()을 사용
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average
  
avg1 = calc_average(1, 2, 3) 
print(avg1) #2.0
avg2 = calc_average(1, 2, 3, 4) 
print(avg2) #2.5

