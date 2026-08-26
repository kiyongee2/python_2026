
# 라우팅
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello~ Flask"

@app.route('/login')
def login():
  return "<h2>로그인 페이지</h2>"


app.run(debug=True)