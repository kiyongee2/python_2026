
"""
# 정보 은닉(Encapsulation)을 활용한 은행 계좌 클래스 예제
  - 정보 은닉은 객체의 내부 상태를 외부에서 직접 접근하지 못하도록 숨기는 것을 의미합니다.
  - 이를 통해 객체의 상태를 보호하고, 객체의 메서드를 통해서만 상태를 변경할 수 있도록 합니다.
  - 이 예제에서는 은행 계좌 클래스(BankAccount)를 정의하고, 계좌 번호, 계좌 소유자, 잔액을 은닉하여 관리합니다.
"""

class BankAccount:
    def __init__(self):
        self.__account_number = None  # 계좌 번호
        self.__account_holder = None  # 계좌 소유자
        self.__balance = 0  # 잔액
        
    # 계좌번호 설정자 메서드
    def set_account_number(self, account_number):
        self.__account_number = account_number
        
    # 계좌번호 접근자 메서드
    def get_account_number(self):
        return self.__account_number
      
    # 계좌 소유자 설정자 메서드
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder
      
    # 계좌 소유자 접근자 메서드
    def get_account_holder(self):
        return self.__account_holder
      
    # 잔액 설정자 메서드
    def set_balance(self, balance):
        self.__balance = balance
        
    # 잔액 접근자 메서드
    def get_balance(self):
        return self.__balance
        
account1 = BankAccount()
# print(account1.__account_number) # 외부에서 직접 접근 불가

account1.set_account_number("123-456-789")
account1.set_account_holder("장그래")
account1.set_balance(100000)

print("계좌 번호:", account1.get_account_number())
print("계좌 소유자:", account1.get_account_holder())
print("잔액:", account1.get_balance())

