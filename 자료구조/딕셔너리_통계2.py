
# 학생 성적표 프로그램
student_list = [
    {"name": "이대한", "kor": 95, "eng": 80, "math": 80},
    {"name": "박민국", "kor": 80, "eng": 75, "math": 75},
    {"name": "오상식", "kor": 90, "eng": 85, "math": 90}
]

print("학생 성적표")
print("이름\t국어\t영어\t수학\t총점\t평균")
for student in student_list:
    name = student["name"]
    kor = student["kor"]
    eng = student["eng"]
    math = student["math"]
    total = kor + eng + math
    average = total / (len(student) - 1)  # 과목 수로 나누어 평균 계산
    print(f"{name}\t{kor}\t{eng}\t{math}\t{total}\t{average:.2f}")