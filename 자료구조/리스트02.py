# 리스트의 연산 - 개수, 합계, 평균
lst = [10, 20, 30, 40]

# 요소의 개수
print(len(lst)) #4

# 요소의 합계
total = lst[0] + lst[1] + lst[2] + lst[3]
print(total) #100

# 반복문으로 요소의 합계 구하기
total = 0  # 합계 초기화(필수)
for item in lst:
    # print(item)
    # total = total + item
    total += item
print("요소의 합계:", total)
"""
   1회전 item -> 10
   2회전 item -> 20
   3회전 item -> 30
   4회전 item -> 40 
"""

# 평균 = 합계 / 개수
average = total / len(lst)
print("요소의 평균:", average) #25.0

# 최대값
max_value = lst[0]  # 최대값 초기화(필수)
for item in lst:
    if item > max_value:
        max_value = item
print("요소의 최대값:", max_value) #40

# 최소값
min_value = lst[0]  # 최소값 초기화(필수)
for item in lst:
    if item < min_value:
        min_value = item
print("요소의 최소값:", min_value) #10

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


