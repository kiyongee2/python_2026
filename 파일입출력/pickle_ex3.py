import pickle

data = {
  "이름": "홍길동", 
  "점수": [90, 85, 100]
}

# 객체 저장 (바이너리 모드)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# 객체 그대로 복원
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
print(type(loaded))   # 딕셔너리 그대로!