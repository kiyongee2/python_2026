
# 학생 성적표 프로그램
student_list = [
    {"name": "이대한", "kor": 95, "eng": 80, "math": 80},
    {"name": "박민국", "kor": 80, "eng": 75, "math": 75},
    {"name": "오상식", "kor": 90, "eng": 85, "math": 90}
]

# 학생 리스트 출력
print("첫 번째 요소 검색:", student_list[0])
print("첫 번째 학생의 이름:", student_list[0]["name"])

print("학생 성적표")
print("이름\t국어\t영어\t수학")
for student in student_list:
    name = student["name"]
    kor = student["kor"]
    eng = student["eng"]
    math = student["math"]
    print(f"{name}\t{kor}\t{eng}\t{math}")
    
    