partnum=10 #爬行的节数
import turtle
turtle.setup(1200,350,100,200)
turtle.penup()
turtle.fd(-550)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor(0.25,0.38,0.96)
turtle.seth(-40)
for i in range(partnum):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
