
print("♠ 컴퓨터 용어 사전 ♠")

dic = {
    "이진수": "0과 1로 이루어진 수 체계",
    "변수": "데이터를 저장하기 위해 이름을 붙인 공간",
    "RAM": "Random Access Memory - 임의 접근 메모리",
    "CPU": "Central Processing Unit - 중앙 처리 장치"
}

while True:
    word = input("검색할 용어를 입력하세요 (종료: q or Q): ")
    if word.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
    elif word in dic:
        # print(f"{word}: {dic[word]}")
        print(f"{word}: {dic.get(word)}") 
    else:
        print(f"'{word}'은(는) 사전에 없습니다.")

'''
while True:
    word = input("검색할 용어를 입력하세요 (종료: q or Q): ")
    if word.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
    # dic.get() 메서드를 사용하여 단어 검색
    definition = dic.get(word)
    if definition:
        print(f"{word}: {definition}")
    else:
        print(f"'{word}'은(는) 사전에 없습니다.")
'''