# if문 
# 조건 - 나이가 20세 미만이면 "미성년자입니다." 출력
'''
age = 18
if age < 20:
    print("미성년자입니다")
    
print(f"나이는 {age}세 입니다.")
'''
# 조건 - 나이가 20세 미만이면 "미성년자입니다"를 출력하고,
#        아니면 "성인입니다." 출력
# 콜론(:)은 블럭의 시작을 의미. 4칸 들여쓰기(인덴트)
age = 22
if age < 20:
    print("미성년자입니다.")
else:
    print("성인입니다.")
print(f"나이는 {age}세 입니다.")

# 좌석의 줄 수 계산
customer = int(input("입장객 수 입력: "))
column = int(input("좌석 열 수 입력: "))

if customer % column == 0:
    row = customer // column
else:
    # row = customer // column + 1
    row = int(customer / column) + 1

print(f"필요한 좌석의 줄 수: {row}줄")

"""
# 다중 조건문(if ~ elif ~ else문)
# 신호등("빨강"-정지, "노랑"-주의, "초록"-진행)
color = input("신호등 색상 입력(빨강/노랑/초록): ")

if color == "빨강":
    print("정지")
elif color == "노랑":
    print("주의")
elif color == "초록":
    print("진행")
else:
    print("잘못된 입력입니다.")
"""


'''
조건 
 컴활 필기점수는 60점 이상이고, 
 실기점수는 70점 이상이면 합격
'''

필기 = int(input("필기 점수 입력(0~100): "))
실기 = int(input("실기 점수 입력(0~100): "))

if 필기 >= 60 and 실기 >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")


# 실습 문제 - 학점 계산 프로그램
'''
score = int(input("점수를 입력하세요: ")) #점수
grade = '' #학점

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"학점은 {grade}입니다.")
'''





























    
