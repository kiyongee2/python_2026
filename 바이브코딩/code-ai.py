# 1부터 10까지 홀수의 합
sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        sum += i
        
print("1부터 10까지 홀수의 합:", sum)

# 센티미터를 미터로 바꾸는 함수
def cm_to_m(cm):
    return cm / 100
  
# 예시 사용
centimeters = 250
meters = cm_to_m(centimeters)
print(f"{centimeters} 센티미터는 {meters} 미터입니다.")