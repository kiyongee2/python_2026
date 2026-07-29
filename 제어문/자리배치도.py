
# 좌석 번호 출력하기 - 4줄 4열
for i in range(1, 5):
  for j in range(1, 5):
    print(4*(i-1) + j, end=" ")
  print()
print()
  
# 15번까지만 출력
for i in range(1, 5):
  for j in range(1, 5):
    seat_number = 4 * (i - 1) + j
    if seat_number > 15:
      break
    print(seat_number, end=" ")
  print()
  
# 자리 배치도
print("*** 자리 배치도 ***")
customer = int(input("입장객 수 입력: "))
column = int(input("좌석 열 수 입력: "))

if customer % column == 0:
    row = customer // column
else:
    # row = customer // column + 1
    row = int(customer / column) + 1

for i in range(1, row + 1):
  for j in range(1, column + 1):
    seat_number = column * (i - 1) + j
    if seat_number > customer:
      break
    print(seat_number, end=" ")
  print()
  
  