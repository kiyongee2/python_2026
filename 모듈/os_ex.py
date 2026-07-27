
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)

# 디렉토리 내 파일 및 폴더 목록 확인
items = os.listdir(current_dir)
print("디렉토리 내 항목:", items)

# 새로운 디렉토리 생성
new_dir = os.path.join(current_dir, "new_folder")
os.mkdir(new_dir)
print("새로운 디렉토리 생성:", new_dir) 

# 경로 관련 정보 확인
print("경로 존재 여부:", os.path.exists('C:/pyworks'))

# 디렉토리 이동
os.chdir('C:/pyworks')
print("현재 작업 디렉토리:", os.getcwd())


