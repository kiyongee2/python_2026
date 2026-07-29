
for i in range(1, 6):
  for j in range(1, 6):
    print('*', end='')
  print()
  
for i in range(5):
  for j in range(5):
    print('*', end='')
  print()
  
for i in range(1, 6):
  for j in range(1, i+1):
    print('*', end='')
  print()
  
for i in range(1, 6):
  for j in range(1, 7-i):
    print('*', end='')
  print()
  
# 전체 줄(행)을 5번 반복합니다.
for i in range(1, 6):

    # 먼저 공백을 출력합니다.
    # 첫 줄은 공백 4개, 둘째 줄은 3개 ... 마지막 줄은 0개입니다.
    for j in range(5 - i):
        print(" ", end="")

    # 별(*)을 출력합니다.
    # 첫 줄은 별 1개, 둘째 줄은 2개 ... 마지막 줄은 5개입니다.
    for k in range(i):
        print("*", end="")

    print() # 한 줄이 끝났으므로 줄을 바꿉니다.
    
for i in range(1, 5):
  for j in range(1, i+1):
    print(j, end=' ')
  print()
print()

for i in range(1, 6):
  for j in range(1, i+1):
    print('*', end='')
  print()

for i in range(1, 6):
  for j in range(1, 6):
    n = 5*(i-1)+j
    if n > 23: break
    print(n, end=' ')
  print()
  
for row in "ABC":
  for col in range(1, 5):
    print(row + str(col), end=" ")
  print()