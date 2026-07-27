
print("♠ 컴퓨터 용어 사전 ♠")

dic = {
    "CPU": "Central Processing Unit - 중앙 처리 장치",
    "RAM": "Random Access Memory - 임의 접근 메모리",
    "HDD": "Hard Disk Drive - 하드 디스크 드라이브",
    "SSD": "Solid State Drive - 솔리드 스테이트 드라이브",
    "GPU": "Graphics Processing Unit - 그래픽 처리 장치"
}

while True:
    word = input("검색할 용어를 입력하세요 (종료하려면 'exit' 입력): ")
    if word.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break
    # 영어인 경우 대문자로 변환하여 검색
    if word.isalpha():
        search_word = word.upper()
    else:
        search_word = word
    # search_word = word.upper() if word.isalpha() else word    
    if search_word in dic:
        print(f"{word}: {dic[search_word]}")
    else:
        print(f"'{word}'은(는) 사전에 없습니다. 다른 용어를 검색해보세요.")