
# 파일 열기 - 읽기 모드
try:
    f = open('c:/pyfile/file1.txt', 'r')

    # 파일에 작성된 문자열 읽기
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)

# 파일 닫기
f.close()

