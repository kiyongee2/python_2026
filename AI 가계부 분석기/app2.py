import pandas as pd

# 천단위 구분 쉼표와 "원"을 붙이는 함수
def show_amount(x):
    return f"{x:,.0f}원"
  
df = pd.read_csv("expenses.csv")
print(df)

print('\n[지출 내역]')
print(df['amount'].apply(show_amount))

print('\n[카테고리별 합계]')
category_amount = df.groupby('category')['amount'].sum()
print(category_amount.apply(show_amount).sort_values(ascending=False))


