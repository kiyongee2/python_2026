
class Car:
  def __init__(self, color, model, wheel):
    self.color = color  #색상
    self.model = model  #모델명
    self.wheel = wheel  #바퀴 수
    
  def drive(self):  # 메서드
    # print(self.color, self.model, "가 달립니다.")
    print(f"{self.color} {self.model}가 달립니다.")
    
car = Car("빨강", "Sonata", 4) #객체(인스턴스) 생성
car.drive()  #메서드 호출
print("바퀴 수:", car.wheel) #속성 접근