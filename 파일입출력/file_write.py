
# 파일 열기 - 쓰기 모드
f = open('c:/pyfile/file1.txt', 'w')

# 파일에 문자열 작성
f.write('Hello Python\n')
f.write('즐거운 하루 되세요~\n')
# f.write(30) # TypeError 발생
f.write(str(30) + '\n') # 숫자를 문자열로 변환하여 작성

# 파일 닫기
f.close()

