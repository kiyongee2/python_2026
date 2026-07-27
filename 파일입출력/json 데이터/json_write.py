
import json
import os

# json 파일 쓰기
new_data = {
    "id": 4,
    "name": "Keyboard",
    "price": 49.99
}

# 현재 파일의 디렉토리 경로를 가져옵니다.
base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'new_products.json'), 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
    
    print("새로운 데이터가 JSON 파일에 저장되었습니다.")