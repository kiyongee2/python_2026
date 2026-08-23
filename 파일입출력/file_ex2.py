# 구구단(2단) 파일에 쓰기
with open("gugu.txt", "w", encoding="utf-8") as f:
    for i in range(1, 10):
        f.write(f"2 x {i} = {2*i}\n")

# 리스트를 저장하고 다시 리스트로 읽기
fruits = ["사과", "바나나", "포도"]
with open("fruits.txt", "w", encoding="utf-8") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

with open("fruits.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
print(lines)