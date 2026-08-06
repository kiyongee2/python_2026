'''
리모컨은 같은 press_power() 메서드를 사용하지만, 
어떤 기기가 전달되느냐에 따라 결과가 달라집니다.
왜 이것이 다형성일까?
리모컨 입장에서는 항상 같은 코드만 실행합니다.
'''

class TV:
  def power(self):
    print("TV 전원이 켜졌습니다.")
    
class AirConditioner:
  def power(self):
      print("에어컨 전원이 켜졌습니다.")
      
class Fan:
  def power(self):
      print("선풍기 전원이 켜졌습니다.")
      
class RemoteControl:
  def press_power(self, device):
    device.power()
    
# 객체 생성
tv = TV()
aircon = AirConditioner()
fan = Fan()

remocon = RemoteControl()

# 같은 버튼
remocon.press_power(tv)
remocon.press_power(aircon)
remocon.press_power(fan)