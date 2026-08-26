
import os

# 현재 작업 디렉터리 확인
current_dir = os.getcwd()
print("현재 작업 디렉터리:", current_dir)

# 디렉터리 내 파일 및 폴더 목록 확인
items = os.listdir(current_dir)
print("디렉터리 내 항목:", items)

# 경로 관련 정보 확인
print("경로 존재 여부:", os.path.exists('D:/python-2026'))

# 디렉터리 이동
os.chdir('D:/python-2026')
print("현재 작업 디렉터리:", os.getcwd())


