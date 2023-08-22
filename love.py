import math
import turtle

turtle.shape("turtle")
turtle.setup(width=900, height=700)
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('red')

def heart1(h):
    return 15 * math.sin(h) ** 3

def heart2(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(4 * h)



for i in range(600):
    x, y = heart1(i) * 20, heart2(i) * 20
    turtle.goto(x, y)

# Draw "I Love You" in the center
turtle.penup()
turtle.goto(0, -45)
turtle.pendown()
turtle.write('I Love You india', align='center', font=('Arial', 50, 'bold'))


turtle.done()