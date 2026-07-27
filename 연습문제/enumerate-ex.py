
# enumerate()로 리스트 항목과 인덱스 출력
colors = ['빨강', '초록', '파랑']
print('\n색상 목록:')
for index, color in enumerate(colors):
    print(f'{index}: {color}')

# enumerate() 예제
fruits = ['사과', '바나나', '체리']
print('과일 목록:')
for index, fruit in enumerate(fruits, start=1):
    print(f'{index}. {fruit}')
    
# enumerate()를 사용하여 딕셔너리 항목 출력
person = {'이름': '홍길동', '나이': 30, '직업': '개발자'}
print('\n개인 정보:')
for index, (key, value) in enumerate(person.items(), start=1):
    print(f'{index}. {key}: {value}')
    
    
    