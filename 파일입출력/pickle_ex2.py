import pickle

nums = [10, 20, 30, 40, 50]

# 리스트를 바이너리 파일로 저장
with open("nums.pkl", "wb") as f:
    pickle.dump(nums, f)

# 바이너리 파일에서 리스트 읽기
with open("nums.pkl", "rb") as f:
    loaded_nums = pickle.load(f)
    print(loaded_nums)
print(f"리스트의 합: {sum(loaded_nums)}")