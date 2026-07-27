# 리스트의 주요 함수
# append() - 요소 추가
a1 = [1, 2, 3, 4, 5]
a2 = []  #빈 리스트 생성

# a1의 요소를 a2에 저장함
for item in a1:
    a2.append(item)
print("a2 =", a2)

# a3 리스트에 a1 요소중 홀수만 저장
a3 = []
for item in a1:
    if item % 2 == 1:
        a3.append(item)
print("a3 =", a3) #a3 = [1, 3, 5]

# 리스트 내포
a4 = [item for item in a1]
print("a4 =", a4) #a4 = [1, 2, 3, 4, 5]

a5 = [item for item in a1 if item % 2 == 1]
print("a5 =", a5) #a5 = [1, 3, 5]

# 리스트 제공 함수
numbers = [5, 2, 9, 1, 5]

# 요소 정렬 - sort()
numbers.sort() #오름차순
print("sort 후:", numbers) #[1, 2, 5, 5, 9]

# 요소 뒤집기 - reverse()
numbers.reverse()
print("reverse 후:", numbers) #[9, 5, 5, 2, 1]

# 리스트 복사 - copy()
copied_numbers = numbers.copy()
print("copy 후:", copied_numbers) #[9, 5, 5, 2, 1]

# 여러개의 요소 추가 - extend(리스트)
# copied_numbers.append(11, 12)  #오류발생
copied_numbers.extend([11, 12])
print("10, 11 추가후:", copied_numbers) # [9, 5, 5, 2, 1, 10, 11, 12]

