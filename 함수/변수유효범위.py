# 변수의 유효 범위(scope)
# 상품의 수량과 가격 출력
"""
# 전역변수 - 메인 영역에서 선언하고 전체 영역에서 값이 유지되고, 
            프로그램이 종료되면 메모리에서 소멸한다. 
# 지역변수 - 제어문(조건, 반복문)과 함수의 블럭안에서 생성되며
            블럭을 벗어나면 메모리에서 소멸한다.
"""
def get_price():
    price = 1000 * quantity  #지역변수(local variable)
    print(f"{quantity}개에 {price}원입니다.")

quantity = 2 #전역 변수(global variable)
get_price()
print(quantity)
# print(price)

# 값이 유지되는 않는 예제
def click_a():
    x = 0  #지역변수
    x = x + 1
    print("x =", x)

click_a() # x = 1
click_a() # x = 1
click_a() # x = 1
print("==========")

# 값이 유지되는 예제
def click_b():
    global x  #지역변수가 전역변수화 함
    x += 1
    print("x =", x)
   
x = 0  #전역변수 
click_b()  #x = 1
click_b()  #x = 2
click_b()  #x = 3

# 배송비 계산 프로그램
# 매개변수 - 단위당 가격, 수량
# 가격이 4만원 미만이면 배송비 3000원 있음
def get_price(unit_price, quantity):
    delivery_fee = 3000 #배송비 
    # 금액 = 단위당 가격 x 수량
    price = unit_price * quantity
    if price < 40000:
        price += delivery_fee #price = price + delivery_fee
    else:
        price
    return price 

price1 = get_price(25000, 2)  #50000
price2 = get_price(30000, 1)  #33000

# 자료형 - 자동형변환(문자열이 숫자보다 크므로 문자열로 형변환)
print("상품1 가격 : " + str(price1) + "원")
print(f"상품1 가격 : {price1}원")

print("상품2 가격 : " + str(price2) + "원")
print(f"상품2 가격 : {price2}원")