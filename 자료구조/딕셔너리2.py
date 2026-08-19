
member = {"name": "이순신", "age":30, "city": "서울"}
member["age"] += 1

print(member["name"])
print(member["age"])

print(f"{member["name"]}")
print(f"{member["city"]}")

# 딕셔너리 예제
print("♠ 컴퓨터 용어사전 ♠")
dic = {
    "CPU": "중앙처리장치",  
    "RAM": "주기억장치",
    "변수": "데이터를 저장하는 메모리 공간",
    "함수": "특정 작업을 수행하는 코드의 집합"
}
word = input("검색할 단어를 입력하세요: ")
if word in dic:
    print(f"{word} : {dic[word]}")
else:
    print(f"{word} : 사전에 없는 단어입니다.")

# 컴퓨터 용어사전 만들기
'''
print("♠ 컴퓨터 용어사전 ♠")
dic = {
    "CPU": "중앙처리장치",  
    "RAM": "주기억장치",
    "변수": "데이터를 저장하는 메모리 공간",
    "함수": "특정 작업을 수행하는 코드의 집합"
}

while True:
    word = input("검색할 단어를 입력하세요(종료:exit): ")
    if word == "exit":
        break
    elif word in dic:
        print(f"{word} : {dic[word]}")
    else:
        print(f"{word} : 사전에 없는 단어입니다.")
'''