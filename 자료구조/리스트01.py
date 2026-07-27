# 리스트 - 여러개의 연속적인 자료를 저장하는 구조
# 첫번째 요소의 인덱스 0부터 시작함, 대괄호([])에 저장함
# 숫자형 리스트
my_list = [10, 20, 30, 40] 
print(my_list) #[10, 20, 30, 40]
print(type(my_list)) #<class 'list'>

# 인덱스(위치)로 요소에 접근
print(my_list[0]) #10
print(my_list[1]) #20
print(my_list[2]) #30
print(my_list[3]) #40
print(my_list[-1]) #40
print(my_list[-2]) #30

# 반복문으로 전체 요소 조회
for item in my_list:
    print(item)

# 요소 변경(수정)
my_list[1] = 50
print(my_list)

# 요소 추가 - 맨 뒤에 추가됨 - append(요소)
my_list.append(100)
print(my_list)

# 요소 삭제 - del 명령어
# del my_list[2] #30 삭제
my_list.remove(30) #값으로 삭제
print(my_list)

# 문자형 리스트
carts = ["라면", "달걀", "커피", "토마토"]
print(carts)
print(type(carts)) #<class 'list'>

# 리스트의 길이(크기)
print(len(carts)) #4

# 요소 조회
print(carts[2]) #"커피"
print(carts[-1]) #"토마토"

# 범위 - 여러개 조회(슬라이싱)
# 종료값-1 인덱스로 조회
print(carts[0:2]) #['라면', '달걀']
print(carts[1:4]) #['달걀', '커피', '토마토']
print(carts[1:]) #['달걀', '커피', '토마토']
print(carts[:]) #['라면', '달걀', '커피', '토마토']

# 전체 요소 조회
for item in carts:
    print(item)

# 요소 변경
carts[2] = "콜라"
print(carts)

# 요소 추가 - 맨 뒤에 추가
carts.append("감자")
print(carts) #['라면', '달걀', '콜라', '토마토', '감자']

# 요소 삭제 - remove(요소) /pop()
carts.remove("달걀")
print(carts)

last_item = carts.pop() # 맨 뒤에서 삭제
print("삭제된 아이템:", last_item) #감자
print(carts) #['라면', '콜라', '토마토']

