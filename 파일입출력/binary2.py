
with open("output/mouse.png", "rb") as f1:
    data = f1.read()
  
with open("output/mouse_copy.png", "wb") as f2:
    f2.write(data)