
import turtle as t

def turn_right():
  t.setheading(0) # 오른쪽을 향하도록 설정
  t.forward(10)
  
def turn_up():
  t.setheading(90) # 위쪽
  t.forward(10)
  
def turn_left():
  t.setheading(180) # 왼쪽
  t.forward(10)
  
def turn_down():
  t.setheading(270) # 아래쪽
  t.forward(10)
 
t.shape("turtle") 
# 오른쪽 방향키를 누르면 turn_right 함수가 실행
t.onkeypress(turn_right, "Right") 
t.onkeypress(turn_up, "Up") # 위쪽 방향키
t.onkeypress(turn_left, "Left") # 왼쪽 방향키
t.onkeypress(turn_down, "Down") # 아래쪽 방향키
t.listen() # 키보드 입력을 받을 준비

t.mainloop()

