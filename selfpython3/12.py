import turtle
t = turtle.Turtle()
s = turtle. Screen()
s. bgcolor('black')
t. speed(0) 
col=("yellow", "red", "pink","cyan", "light green", "blue")
for i in range(150):
    t. pencolor (col[1%5])
    t. circle(190-i/2,90)
    t.lt(40)
    t. circle(190-1/3,40)
    t.lt(40)
s. exitonclick()