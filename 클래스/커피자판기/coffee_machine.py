
class CoffeeMachine:
    def __init__(self):
        self.balance = 0
        self.coffee_stock = 10
        self.coffee_price = 300

    def insert_coin(self, money):
        self.balance += money
        print(f"{money}원을 넣었습니다.")

    def make_coffee(self):
        if self.balance < self.coffee_price:
            print("잔액이 부족합니다.")
            return

        if self.coffee_stock == 0:
            print("커피가 없습니다.")
            return

        self.balance -= self.coffee_price
        self.coffee_stock -= 1

        print("☕ 커피가 나왔습니다.")

    def return_change(self):
        print(f"잔돈 {self.balance}원을 반환합니다.")
        self.balance = 0
       
# 자판기 사용 
machine = CoffeeMachine()
machine.insert_coin(500)
machine.make_coffee()
machine.return_change()