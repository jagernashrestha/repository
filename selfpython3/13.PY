import turtle
t = turtle.Turtle()
s = turtle. Screen()
s. bgcolor('black')
t. speed(0) 
col=("yellow", "red", "pink","cyan", "light green", "blue")
for i in range(150):
    t. pencolor (col[1%5])
    t. circle(190-i/2,90)
    t.lt(90)
    t. circle(190-1/3,160)
    t.lt(60)
s. exitonclick()