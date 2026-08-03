
# 이차원 리스트 - 행과 열로 이루어진 리스트
a = [
    [1, 2, 3],
    [4, 5, 6]
]

print(a[0])
print(a[1])
print(a[1][1])

for row in a:
    for x in row:
        print(x, end=" ")
    print()

# 리스트 생성
matrix = [
    [1, 2, 3],  #1행
    [4, 5, 6]   #2행
]

# 출력
print(matrix) #[[1, 2, 3], [4, 5, 6]]
print(type(matrix)) #<class 'list'>

# 특정 행 출력
print(matrix[0]) #[1, 2, 3]
print(matrix[1]) #[4, 5, 6]

# 특정 값 출력
print(matrix[0][0]) # 0행 0열, 1
print(matrix[0][1]) # 0행 1열, 2
print(matrix[1][2]) # 1행 2열, 6

# 전체 값 출력
for row in matrix:  #행
    for val in row: #열 - 0행 [1, 2, 3], 1행 [4, 5, 6]
        print(val, end=" ") #1 2 3 4 5 6
    print() #행이 끝날 때 줄바꿈
    
# 요소 변경
matrix[0][1] = 20

# 요소 추가
matrix.append([7, 8, 9]) #3행에 [7, 8, 9] 추가
print(matrix) #[[1, 20, 3], [4, 5, 6], [7, 8, 9]]

# 요소 삭제
del matrix[1] #2행 삭제
print(matrix) #[[1, 20, 3], [7, 8, 9]]

