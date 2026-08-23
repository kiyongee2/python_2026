# 이미지 읽고 쓰기
with open("output/mouse.png", "rb") as src:
    data = src.read()
  
with open("output/mouse_copy.png", "wb") as dst:
    dst.write(data)
    
print(f"복사 완료! 복사한 파일 크기: {len(data)} bytes")