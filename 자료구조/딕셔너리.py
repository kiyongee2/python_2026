# 딕셔너리 - 여러개의 값을 저장함
# 키(Key)와 값(value)의 쌍으로 이루어짐 - 키는 따옴표로 감싼다.
# 중괄호({}) 사용함

student = {
  "name": "한강", 
  "age": 21, 
  "university": "한강대학교"
}

print(student) #{'name': '한강', 'age': 21, 'university': '한강대학교'}
print(type(student)) #<class 'dict'>

# 요소에 접근(검색)
# 1. 방법1
print(student["name"]) #한강
print(student["age"]) #21
print(student["university"]) #한강대학교

# 2. 방법2 - get(key)
print(student.get("name"))
print(student.get("age"))
print(student.get("university"))

# 요소 추가
student["major"] = "전자공학과"
print(student)

# 요소 수정
student["age"] = 31
print(student)

# 요소 삭제 - pop(key)
student.pop("university")
print("요소 삭제후 딕셔너리:", student)

print(list(student.keys())) #['name', 'age', 'major']
print(list(student.values())) #['한강', 31, '전자공학과']

# 키, 값 목록
keys = student.keys()
values = student.values()
print("키 목록:", keys) #키 목록: dict_keys(['name', 'age', 'major'])
print("값 목록:", values) #값 목록: dict_values(['한강', 31, '전자공학과'])

for key in student.keys():
    print(key, ":", student[key])

# 딕셔너리 예제
fruit = {"apple": "red", "banana": "yellow"}
print(fruit)

# grape:blue 추가
fruit["grape"] = "blue"
print(fruit)

# banana키로 yellow 검색하기
# 1.
print(fruit.get("banana"))
# 2.
print(fruit["banana"])

# 예제
dic = {}  #빈 딕셔너리
dic[1] = 'a'
dic[2] = 'b'
dic[3] = 'c'

print(dic) #{1: 'a', 2: 'b', 3: 'c'}