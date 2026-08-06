# 상속과 다형성
# 부모 클래스
class Device:
    def power(self):
        print("기기의 전원이 켜졌습니다.")


# 자식 클래스
class TV(Device):
    def power(self):
        print("📺 TV 전원이 켜졌습니다.")


class AirConditioner(Device):
    def power(self):
        print("❄️ 에어컨 전원이 켜졌습니다.")


class Fan(Device):
    def power(self):
        print("🌀 선풍기 전원이 켜졌습니다.")


# 리모컨 클래스
class RemoteControl:
    def press_power(self, device):
        device.power()


# 객체 생성
tv = TV()
aircon = AirConditioner()
fan = Fan()

remote = RemoteControl()

# 같은 버튼으로 여러 기기 제어
remote.press_power(tv)
remote.press_power(aircon)
remote.press_power(fan)