d = [
  [90,80],
  [70,100],
  [60,75]
]

print(d[0])
print(d[1])
print(d[2])

print(d[0][0])
print(d[0][1])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])

for row in d:
  for i in row:
    print(i)
    
# 학생별 총점(행 방향)
for row in d:
  print(sum(row))
  
# 과목별 총점(열방향)과 평균
for col in range(2):
  total = d[0][col] + d[1][col] + d[2][col]
  # print("과목", col + 1, "평균:", total / 3)
  print(f"과목 {col + 1} 평균: {total / 3}")
 