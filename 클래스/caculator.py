
class Calculator:

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        # y가 0이면 나눗셈을 할 수 없음
        if y == 0:
            return "0으로 나눌 수 없습니다"

        return x / y

# 계산기 객체 생성
calc = Calculator()

print(calc.add(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))

# y가 0인 경우
print(calc.div(10, 0))