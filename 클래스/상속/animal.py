
class Animal:
    def breathe(self):
        print("숨을 쉽니다.")
        
    def speak(self):
        raise NotImplementedError("서브 클래스에서 speak 메서드를 구현해야 합니다.")
      
class Dog(Animal):
    '''
    def speak(self):
        return "멍멍!"
    '''
        
class Cat(Animal):
    def speak(self):
        return "야옹!"
      
# 동물 객체 생성
try:
  dog = Dog()
  cat = Cat()

  # 동물 정보 출력
  print("강아지 정보:")
  dog.breathe()  # 숨을 쉽니다.
  print(dog.speak())  # 멍멍!
  print("\n고양이 정보:")
  cat.breathe()  # 숨을 쉽니다.
  print(cat.speak())  # 야옹!
except NotImplementedError as e:
  print(e)  # 서브 클래스에서 speak 메서드를 구현해야 합니다.