from turtle import Turtle, Screen
import turtle
import random
import colorgram



def Hirst():
    turtle.colormode(255)
    

    Michel = Turtle()
    Michel.shape("turtle")
    Michel.pencolor()
    Michel.shapesize(3, 3, 3)
    Michel.pensize(10)
    Michel.speed(5)


    colors = colorgram.extract('docs/hirst.jpg', 10)

    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    Michel.penup()
    Michel.setheading(225)
    Michel.forward(300)
    Michel.setheading(0)
    nb_dots = 100

    for d_count in range(1, nb_dots + 1):
        Michel.dot(20, random.choice(rgb_colors))
        Michel.forward(50)

        if d_count % 10 == 0:
            Michel.setheading(90)
            Michel.forward(50)
            Michel.setheading(180)
            Michel.forward(500)
            Michel.setheading(0)


    screen = Screen()
    #screen.setworldcoordinates(-100, -100, 100, 100)
    screen.exitonclick()

if __name__ == "__main__":
    Hirst()