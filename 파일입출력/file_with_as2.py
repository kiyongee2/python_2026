
# 파일에 리스트 저장하기
carts = ["라면", "달걀", "쌀", "커피"]

# 한글이 깨지는 경우 방지 - > encoding='utf-8' 추가
with open('output/cart.txt', 'w', encoding='utf-8') as f:
    for item in carts:
        f.write(f"{item}\n")
        
# 파일에서 리스트 불러오기
with open('output/cart.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content) # 라면\n달걀\n쌀\n커피\n
    
    # 한 줄씩 읽어서 출력
    # for line in f:
    #     print(line.strip()) #줄바꿈 문자 제거

 