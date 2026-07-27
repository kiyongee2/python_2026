
import turtle as t

t.shape("turtle")

'''
# 사각형
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

# 삼각형
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
'''

"""
# 반복문 사용하기
for i in range(4):
    t.forward(100)
    t.right(90)
    
for i in range(3):
    t.forward(100)
    t.left(120)
"""

# 변수 사용하기
n = 4
d = 100
for i in range(n):
    t.forward(d)
    t.right(360/n)
    
t.color("blue")
n = 3
for i in range(n):
    t.forward(d)
    t.left(360/n)
    
t.color("red")
t.circle(50)


t.mainloop()