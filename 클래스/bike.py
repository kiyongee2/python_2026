
class Bike:
  def __init__(self, color, gears):
    self.color = color
    self.gears = gears
    
  def __str__(self):
    return f"{self.color} 자전거 (기어 {self.gears})"
  
# 자전거 객체(인스턴스) 생성
bike1 = Bike("노랑", 5)
print(bike1)

# 객체 리스트
print("***** 자전거 리스트 *****")
bikes = [Bike("파랑", 7), Bike("검정", 21)]
for bike in bikes:
  print(bike)