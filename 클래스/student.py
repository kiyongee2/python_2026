
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"학생 이름: {self.name}, 학번: {self.student_id}"
      
# 학생 객체 생성
student1 = Student("홍길동", "20260001")
print(student1)  # 학생 이름: 홍길동, 학번: 20260001

# 학생 객체 리스트 생성
students = [
    Student("김철수", "20260002"),
    Student("이영희", "20260003"),
    Student("박민수", "20260004")
]

# 학생 객체 리스트 출력
for student in students:
    print(student)
    # 학생 이름: 김철수, 학번: 20260002
    # 학생 이름: 이영희, 학번: 20260003
    # 학생 이름: 박민수, 학번: 20260004