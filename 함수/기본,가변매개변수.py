
def order_pizza(size="M", *toppings):
    print(f"[{size} 사이즈 피자]")
    if toppings:
        print("토핑:", ", ".join(toppings))
    else:
        print("토핑: 없음 (기본)")
    print("-" * 20)


# 호출 예시
order_pizza()                          # 사이즈 M, 토핑 없음
order_pizza("L")                       # 사이즈 L, 토핑 없음
order_pizza("L", "페퍼로니")            # 사이즈 L, 토핑 1개
order_pizza("XL", "치즈", "베이컨", "올리브")  # 토핑 여러 개