
# subject 모듈에서 Subject 클래스를 가져옵니다.
from subject import Subject

class Student:
    def __init__(self, name, student_id):
        self.name = name # 학생 이름
        self.student_id = student_id # 학번
        self.subjects = [] # 수강 신청한 과목을 저장하는 리스트
     
    # 학생이 과목을 수강 신청하는 메서드
    def enroll(self, subject):
        self.subjects.append(subject)
        
    # 학생의 정보를 출력하는 메서드
    def get_info(self):
        print(f"이름: {self.name}, 학번: {self.student_id}")
        print("수강 과목:")
        for subject in self.subjects:
            print(f"  - {subject.get_info()}")
          
# 과목 객체 생성
computer = Subject("컴퓨터학과", "CS101")
math = Subject("수학과", "MATH201")

# 학생 객체 생성
student1 = Student("홍길동", "S12345")

# 학생이 과목을 수강 신청
student1.enroll(computer)
student1.enroll(math)

# 학생 정보 출력
print(student1.get_info())  
print("----------------------------------------")

# 학생 리스트 객체 생성
subjects = [
    Subject("컴퓨터 과학", "CS101"),
    Subject("수학", "MATH201"),
    Subject("물리학", "PHYS301")
]

# 새로운 학생 객체 생성
student2 = Student("박상희", "S67890")

# 수강 과목과 학생의 정보 출력
for subject in subjects:
    student2.enroll(subject)
    student2.get_info()
    print("----------------------------------------")
    
    