
s = {10, 20, 30}
print(s) #{10, 20, 30}
print(type(s)) #<class 'set'>

# 요소 추가
s.add(40)
print(s) #{40, 10, 20, 30}

s.add(100) #새로운 요소 추가
print(s) #{40, 10, 100, 20, 30}

s.add(20) #중복된 요소 추가(변경없음)
print(s) #{40, 10, 100, 20, 30}

# 요소 삭제
s.remove(20) #20 요소 삭제
print(s) #{40, 10, 100, 30}

# 집합 연산
s1 = {1, 3, 4}
s2 = {3, 4, 5, 6}

# 합집합
print(s1 | s2) #{1, 3, 4, 5, 6}

# 교집합
print(s1 & s2) #{3, 4}

# 차집합
print(s1 - s2) #{1}

s3 = set()
print(s3) #set()
print(type(s3)) #<class 'set'>

# 요소 추가
s3.add(10)
s3.add(20)  
print(s3) #{10, 20}

lst = [1, 2, 2, 3, 4, 4]
unique_set = set(lst) #중복 제거
print(unique_set) #{1, 2, 3, 4}

