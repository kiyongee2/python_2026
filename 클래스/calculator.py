
class Calculator:
    # 덧셈
    def add(self, a, b):
        return a + b

    # 뺄셈
    def subtract(self, a, b):
        return a - b

    # 곱셈
    def multiply(self, a, b):
        return a * b

    # 나눗셈
    def divide(self, a, b):
        if b == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        return a / b
      
# 계산기 객체 생성
calculator = Calculator()
# 덧셈
print(calculator.add(10, 5))  # 15
# 뺄셈
print(calculator.subtract(10, 5))  # 5  
# 곱셈
print(calculator.multiply(10, 5))  # 50
# 나눗셈
# print(calculator.divide(10, 5))  # 2.0
print(calculator.divide(10, 0))  # None


"""
try:
    print(calculator.divide(10, 0))
except ValueError as e:
    print(e)  # 0으로 나눌 수 없습니다.
"""