
with open("output/data.bin", "wb") as f:
    for i in range(10):
        f.write(i.to_bytes(1, byteorder='little'))
        
with open("output/data.bin", "rb") as f:
    data = f.read()
    print(list(data))