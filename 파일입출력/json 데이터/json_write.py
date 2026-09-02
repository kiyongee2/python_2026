
import json
import os

# 추가할 제품 정보
new_product = {
    "id": 4,
    "name": "모니터",
    "price": 1100000
}

# 현재 파일의 디렉토리 경로를 가져옵니다.
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'products.json')

with open(file_path, 'r', encoding='utf-8') as f:
    products = json.load(f)

products.append(new_product)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

print("새로운 데이터가 JSON 파일에 저장되었습니다.")