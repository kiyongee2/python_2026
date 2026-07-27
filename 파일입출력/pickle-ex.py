
# pickle 모듈을 사용하여 데이터를 파일에 저장하고 읽어오는 예제입니다.
import pickle

# 딕셔너리를 파일에 저장합니다.
try:
    with open('./output/data.txt', 'wb') as f:
        dic = {1: '강아지', 2: '고양이', 3: '닭'}
        pickle.dump(dic, f)
except Exception as e:
    print(f"예외 발생: {e}")


# 파일에서 딕셔너리를 읽어옵니다.
try:
    with open('./output/data.txt', 'rb') as f:
        data = pickle.load(f)
        print(data)
except Exception as e:
    print(f"예외 발생: {e}")
    
    