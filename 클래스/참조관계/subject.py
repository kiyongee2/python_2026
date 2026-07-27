
class Subject:
    def __init__(self, name, code):
        self.name = name  # 과목명
        self.code = code  # 과목코드
        
    def get_info(self):
        return f"과목명: {self.name}, 과목코드: {self.code}"
  
if __name__ == "__main__":    
    # 과목 객체 생성
    subject1 = Subject("컴퓨터 과학", "CS101")
    print(subject1.get_info())

    subject2 = Subject("수학", "MATH201")
    print(subject2.get_info())
    
    