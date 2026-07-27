import pandas as pd

df = pd.read_csv("expenses.csv")
print("=== 원본 데이터 ===")
print(df)

# 1. 기본 apply - 금액에 "원" 붙이기
print("\n=== 1. 금액 포맷팅 ===")
print(df['amount'].apply(lambda x: f"{x:,.0f}원"))

# 2. 문자열 변환 - 카테고리 앞에 이모지 붙이기
print("\n=== 2. 카테고리에 이모지 붙이기 ===")
emoji_map = {"식비": "🍚", "교통": "🚇", "카페": "☕", "쇼핑": "🛒"}
print(df['category'].apply(lambda x: f"{emoji_map.get(x, '📌')} {x}"))

# 3. 조건 분기 - 금액 크기에 따라 분류
print("\n=== 3. 금액 크기 분류 ===")
def classify_amount(x):
    if x >= 30000:
        return "고액"
    elif x >= 10000:
        return "중간"
    else:
        return "소액"

df['등급'] = df['amount'].apply(classify_amount)
print(df[['category', 'amount', '등급']])

# 4. DataFrame에 apply (행 단위) - axis=1
print("\n=== 4. 행 단위 apply (axis=1) ===")
def make_summary(row):
    return f"{row['date']} | {row['category']}에서 {row['amount']:,}원 사용 ({row['memo']})"

print(df.apply(make_summary, axis=1))

# 5. DataFrame에 apply (열 단위) - axis=0
print("\n=== 5. 열 단위 apply (axis=0) ===")
print(df[['amount']].apply(['sum', 'mean', 'max', 'min']))

# 6. map vs apply 비교
print("\n=== 6. map으로도 가능 (Series 전용) ===")
print(df['amount'].map(lambda x: x * 1.1))  # 10% 인상
