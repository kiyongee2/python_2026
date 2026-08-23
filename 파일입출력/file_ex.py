
# 쓰기 (w: 새로 만들거나 덮어쓰기)
f = open("file.txt", "w", encoding="utf-8")
f.write("안녕하세요\n")
f.write("파이썬 파일 입출력\n")
f.close()

# 추가 (a: 기존 내용 뒤에 붙임)
f = open("file.txt", "a", encoding="utf-8")
f.write("한 줄 더 추가\n")
f.close()

# 읽기 (r)
f = open("file.txt", "r", encoding="utf-8")
print(f.read())
f.close()

# 예외 처리
try:
    f = open("file.txt", "r", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
finally:
    f.close()
