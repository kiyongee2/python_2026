import pandas as pd

# 샘플 데이터 생성 또는 CSV 불러오기
# CSV 형식: date,category,amount,memo
# 예: 2026-04-01,식비,12000,점심

FILE = 'expenses.csv'

try:
    df = pd.read_csv(FILE)
except FileNotFoundError:
    sample = [
        ['2026-04-01','식비',12000,'점심'],
        ['2026-04-01','교통',2500,'지하철'],
        ['2026-04-02','카페',15500,'커피'],
        ['2026-04-03','식비',18000,'저녁'],
        ['2026-04-04','쇼핑',43000,'생활용품'],
    ]
    df = pd.DataFrame(sample, columns=['date','category','amount','memo'])

print('\n[지출 내역]')
print(df)

print('\n[카테고리별 합계]')
print(df.groupby('category')['amount'].sum().sort_values(ascending=False))

monthly_total = df['amount'].sum()
print(f'\n총 지출: {monthly_total:,}원')

# 간단한 AI 스타일 분석 규칙
advice = []
category_sum = df.groupby('category')['amount'].sum().to_dict()
# print(category_sum) #{'교통': 2500, '쇼핑': 43000, '식비': 30000, '카페': 15500}

print(category_sum.get('카페',0)) # 카페 지출이 없을 때 0 반환
if category_sum.get('카페',0) > 10000:
    advice.append('카페 지출이 높습니다. 텀블러 사용이나 횟수 조절을 추천합니다.')
if category_sum.get('식비',0) > monthly_total * 0.4:
    advice.append('식비 비중이 높습니다. 주간 예산을 설정해보세요.')
if category_sum.get('쇼핑',0) > 30000:
    advice.append('쇼핑 지출이 큽니다. 필요/충동 구매를 구분해보세요.')
if not advice:
    advice.append('지출 패턴이 안정적입니다. 현재 소비 습관을 유지하세요.')

print('\n[AI 소비 분석 리포트]')
# 1부터 시작하는 번호와 함께 조언 출력
for i, a in enumerate(advice,1):
    print(f'{i}. {a}')

print('\n[절약 목표 제안]')
print(f'다음 달 목표 지출: {int(monthly_total*0.9):,}원 (10% 절감)')


# csv 파일로 저장
df.to_csv(FILE, index=False)

