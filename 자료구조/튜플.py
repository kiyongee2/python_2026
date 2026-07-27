"""
# 튜플 
  - 여러 개의 값을 저장하는 자료구조
  - 소괄호 () 사용
  - 조회(검색)는 리스트와 동일하게 가능
  - 요소(값)의 수정, 삭제 불가
"""

# 튜플 생성
t1 = (1, 2, 3)
print(t1)
print(type(t1)) #<class 'tuple'> 

# 특정 요소 조회
print(t1[0]) #1
print(t1[1]) #2
print(t1[-1]) #3

# 슬라이싱
print(t1[1:3]) #(2,3)
print(t1[:]) #(1,2,3)

# t1[1] = 5 # 변경 불가
# del t1[2] #삭제 불가

# 요소 1개 생성 - 쉼표를 붙임
# 정수
t2 = (10)
print(t2) #10
print(type(t2))

t2 = (10,)
print(t2) #(10,)
print(type(t2))

# 튜플 결합
t3 = t1 + t2
print(t3) #(1, 2, 3, 10)

# 점수 저장
# 점수 리스트에 튜플로 저장
scores = [] #빈 리스트 생성

# 점수 저장
scores.append((80,))
scores.append((70,))
scores.append((90,))

# 점수 조회
print(scores) #[(80,), (70,), (90,)]

# 과목 리스트 생성 : 과목이름, 점수
subjects= []

# 과목 저장
subjects.append(("국어", 90))
subjects.append(("수학", 80))

# 과목 조회
print(subjects) #[('국어', 90), ('수학', 80)]
print(subjects[0]) #('국어', 90)
print(subjects[1]) #("수학", 80)

# 특정 요소 조회
print(subjects[0][0]) #국어
print(subjects[0][1]) #90
print(subjects[1][0]) #수학
print(subjects[1][1]) #80

# 전체 조회(for)
for row in subjects:
    print(row)