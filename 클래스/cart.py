
# 장바구니 클래스 정의  
class Cart:
    # 초기화 메서드
    def __init__(self):
        self.items = []  # 아이템을 저장하는 리스트

    # 아이템 추가 메서드
    def add_item(self, item): 
        self.items.append(item)

    # 아이템 제거 메서드
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    # 아이템 조회 메서드
    def get_items(self):
        return f"장바구니: {self.items}"

cart = Cart()  # 장바구니 객체 생성
cart.add_item("사과")
cart.add_item("바나나")
print(cart.get_items())  # 장바구니: ['사과', '바나나']

cart.remove_item("사과")
print(cart.get_items())  # 장바구니: ['바나나'] 

