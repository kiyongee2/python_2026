'''
print(range(5))
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(0, 10, 2)))

for i in range(1, 6):
    print(i, end=" ")
'''

# 1부터 10까지의 짝수 출력(if문 사용)
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")
print()  # 줄바꿈

# 1부터 10까지의 짝수 출력
for i in range(2, 11, 2):
    print(i, end=" ")

total = 0
for i in range(1, 11):
    total += i
print(f"\n1부터 10까지의 합: {total}\n")

# 구구단 2단 출력
dan = 2
for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")  
    
# 중첩 for문
for i in range(3):
    for j in range(2):
        print(f"{i}, {j}")
        
# 별 모양
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()  # 줄바꿈
    
rows= 4
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()  # 줄바꿈
    
# 구구단 2단부터 9단까지 출력
# for dan in range(2, 10):
#     for i in range(1, 10):
#         result = dan * i
#         print(f"{dan} x {i} = {result}")
#     print()  # 단이 끝날 때마다 줄바꿈
    
# 구구단 응용 
# for dan in range(2, 10):
#     if dan % 2 == 0:  # 짝수 단만 출력
#         for i in range(1, 10):
#             result = dan * i
#             print(f"{dan} x {i} = {result}")
#         print()  # 단이 끝날 때마다 줄바꿈 

# 구구단 응용 
# for dan in range(2, 10):
#     for i in range(1, dan + 1):
#       print(f"{dan} x {i} = {dan * i}")
#     print()  # 단이 끝날 때마다 줄바꿈
    
for dan in range(2, 10):
    for i in range(1, 10):
      if i > dan:
        break
      print(f"{dan} x {i} = {dan * i}")
    print()  # 단이 끝날 때마다 줄바꿈