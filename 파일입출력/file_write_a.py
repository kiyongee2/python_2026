
# try-except-finally 구문을 사용

# 파일 열기 - 추가 모드
try:
  f = open('c:/pyfile/file1.txt', 'a')

  # 파일에 문자열 작성
  f.write('추가된 내용입니다.\n')
  f.write('Hello World\n')
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)

finally:
  if 'f' in locals(): # 파일이 열렸는지 확인
    f.close()


