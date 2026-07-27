
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"안녕하세요, 제 이름은 {self.name}입니다."
      
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # 부모 클래스의 초기화 메서드 호출
        self.employee_id = employee_id

    def introduce(self):
        return f"안녕하세요, 제 이름은 {self.name}이고, 사원 번호는 {self.employee_id}입니다."
      
# Person 객체 생성
person = Person("홍길동")
print(person.introduce())  # 안녕하세요, 제 이름은 홍길동입니다.

# Employee 객체 생성
employee = Employee("김철수", "E12345")
print(employee.introduce())  # 안녕하세요, 제 이름은 김철수이고, 사원 번호는 E12345입니다.