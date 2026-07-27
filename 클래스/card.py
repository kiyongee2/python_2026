
# 카드 클래스 정의
class Card:
    def __init__(self):
      self.card_number = 0
      self.card_number = self.card_number + 1
      
card1 = Card()
print(card1.card_number) # 1

card2 = Card()
print(card2.card_number) # 1

card3 = Card()
print(card3.card_number) # 1

# 카드번호 자동 증가를 위해 클래스 변수 사용
class Card:
    card_number = 0 # 클래스 변수로 카드 번호 초기화
    
    def __init__(self, owner):
        Card.card_number += 1 # 클래스 변수를 증가시킴
        
        # 인스턴스 변수에 현재 카드 번호 할당
        self.card_number = Card.card_number 
        self.owner = owner
        
card1 = Card("이순신")
print(card1.card_number) # 1

card2 = Card("김선화")
print(card2.card_number) # 2

card3 = Card("고담덕")
print(card3.card_number) # 3

