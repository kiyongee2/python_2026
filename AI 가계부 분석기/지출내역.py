
import pandas as pd

# 지출내역.xlsx 파일을 읽어오기
df = pd.read_excel("지출내역.xlsx")

# print(df)
print(df.head())

df.info() # 데이터프레임 정보 확인

print('\n[지출 내역]')
print(df['지출액'])

print('\n[카테고리별 합계]')
print(df.groupby('분류')['지출액'].sum().sort_values(ascending=False))

monthly_total = df['지출액'].sum()
print(f'\n총 지출: {monthly_total:,}원')


