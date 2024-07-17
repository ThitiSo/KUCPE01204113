import turtle
turtle.speed(0)
turtle.pensize(20)

turtle.goto(0,-300)
turtle.color('green')
turtle.goto(0,0)

turtle.pensize(0)
colorpicks=['green','red','yellow','pink','purple','orange','blue','gray']
for i in range(8):
    turtle.color('black',colorpicks[i])
    turtle.begin_fill()
    turtle.circle(60)
    turtle.left(45)
    turtle.end_fill()
turtle.goto(0,-40)
turtle.color('black','yellow')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.done()
