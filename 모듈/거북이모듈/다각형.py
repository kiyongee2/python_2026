
import turtle as t

t.shape("turtle")

def polygon(n):
  for x in range(n):
    t.forward(100)
    t.left(360/n)
    
def polygon2(n, d):
  for x in range(n):
    t.forward(d)
    t.left(360/n)

t.color("blue")    
polygon(3)

t.penup()
t.goto(150, 0) # 거북이 위치 이동

t.pendown()
t.color("red")
polygon2(5, 100)

t.mainloop()

