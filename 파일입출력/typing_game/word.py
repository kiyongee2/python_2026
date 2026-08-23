# 단어 파일 만들기
words = ["python", "programming", "challenge", "developer", "algorithm"]
try:
    with open("typing_game/word.txt", "w") as f:
        for word in words:
            f.write(word + "\n")
except FileNotFoundError :
    print("파일이 존재하지 않습니다.")
  
try:
    with open("typing_game/word.txt", "r") as f:
        # strip() 메서드를 사용하여 각 줄의 공백 제거
        word_list = [line.strip() for line in f]  
except FileNotFoundError :
    print("파일이 존재하지 않습니다.")

# print(word_list)  # 단어 리스트 출력
for word in word_list:
    print(word)  # 단어 하나씩 출력