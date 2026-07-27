
# json 파일 읽기
import json
import os

# 현재 파일의 디렉토리 경로를 가져옵니다.
base_dir = os.path.dirname(os.path.abspath(__file__))

# json 파일 경로를 설정합니다.
file = os.path.join(base_dir, 'products.json')

# json 파일을 읽어서 데이터를 출력합니다.
with open(file, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)

# 제품 정보 출력
print("\n첫 번째 제품 정보")
print("-" * 50)
print(f"ID: {data[0]['id']}")
print(f"Name: {data[0]['name']}")
print(f"Price: {data[0]['price']}")
print(f"Description: {data[0]['description']}")
print(f"Image: {data[0]['image']}")

print("\n제품 목록")
print("-" * 50)
for product in data:
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Description: {product['description']}")
    print(f"Image: {product['image']}")
    print("-" * 50)