# 학점 계산 프로그램
score = int(input("점수: "))

'''
if score < 0 or score > 100:
    print("점수는 0보다 크고  100보다 작은 숫자를 입력해 주세요")
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
'''

if score < 0 or score > 100:
    print("점수는 0보다 크고  100보다 작은 숫자를 입력해 주세요")

if score >= 90:
    if score >= 97:
        grade = 'A+'
    elif score >= 93:
        grade = 'A0'
    else:
        grade = 'A-'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'  
print("학점:", grade)














