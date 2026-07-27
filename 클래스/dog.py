
class Dog:
    kind = '말티즈' # 클래스 변수
    
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        return f"{self.name}가 짖습니다. 멍멍!"
      
# 강아지 객체 생성
dog1 = Dog("코코")
dog2 = Dog("콩이")

# 강아지 정보 출력
# 종류: 클래스 이름으로 접근
print(f"Dog1의 이름: {dog1.name}, 종류: {Dog.kind}")  
print(f"Dog2의 이름: {dog2.name}, 종류: {Dog.kind}")

# 강아지 짖는 소리 출력
print(dog1.bark())  # 코코가 짖습니다. 멍멍!
print(dog2.bark())  # 콩이가 짖습니다. 멍멍!