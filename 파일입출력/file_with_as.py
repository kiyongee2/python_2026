
# 구구단을 파일로 저장하기
with open('c:/pyfile/gugudan.txt', 'w') as f:
    for i in range(2, 10):
        for j in range(1, 10):
            f.write(f"{i} x {j} = {i*j}\n")
        f.write("\n")
# 파일 닫기는 with 블록이 끝나면 자동으로 처리됩니다.

# 파일 열기 - 읽기 모드
try:
    with open('c:/pyfile/gugudan.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)
    
