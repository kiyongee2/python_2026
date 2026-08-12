# 1부터 100까지 숫자 중 짝수의 합을 구해서 출력
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print(sum_even)

# 섭씨를 화씨로 바꾸는 함수
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
  
