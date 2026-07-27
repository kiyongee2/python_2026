# 카드 번호가 자동 증가하는 클래스 정의
class Card:
    # 클래스 변수로 카드 번호 초기화
    card_number = 0

    def __init__(self):
        # 카드 번호를 1씩 증가시키며 할당
        Card.card_number += 1
        self.number = Card.card_number
        
# 카드 객체 생성
card1 = Card()
card2 = Card()
card3 = Card()

# 카드 번호 출력
print(f"Card 1 번호: {card1.number}")  # Card 1 번호: 1
print(f"Card 2 번호: {card2.number}")  # Card 2 번호: 2
print(f"Card 3 번호: {card3.number}")  # Card 3 번호: 3

