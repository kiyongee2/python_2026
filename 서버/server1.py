# server1.py
# flask 모듈에서 Flask 클래스를 가져옴
from flask import Flask

app = Flask(__name__) # app 객체 생성

""" '/' 경로에 대한 요청이 들어오면 
home() 함수를 실행하도록 라우팅 설정
http://127.0.0.1:5000/ """
@app.route('/')  
def home():
    return '<h1>Hello, World!</h1>'
  
# Flask 애플리케이션을 실행, debug 모드 활성화
if __name__ == '__main__':
    app.run(debug=True) 
    
    