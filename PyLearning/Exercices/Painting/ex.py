import os
from turtle import Turtle, Screen
import turtle
import random
import colorgram

def Hirst():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    image_path = os.path.join(base_dir, 'docs', 'hirst.jpg')

    screen = Screen()
    screen.clearscreen()
    turtle.colormode(255)
    
    Michel = Turtle()
    Michel.shape("turtle")
    Michel.shapesize(2,2,2)
    Michel.speed(0)
    Michel.penup()

    try:
        colors = colorgram.extract(image_path, 10)
        rgb_colors = []
        for color in colors:
            rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    except FileNotFoundError:
        print(f"DEBUG: Path tried -> {image_path}")
        rgb_colors = [(202, 164, 109), (150, 75, 49), (223, 201, 135), (238, 240, 245)]

    Michel.setheading(225)
    Michel.forward(300)
    Michel.setheading(0)
    
    for d_count in range(1, 101):
        Michel.dot(20, random.choice(rgb_colors))
        Michel.forward(50)
        if d_count % 10 == 0:
            Michel.setheading(90)
            Michel.forward(50)
            Michel.setheading(180)
            Michel.forward(500)
            Michel.setheading(0)

    screen.exitonclick()