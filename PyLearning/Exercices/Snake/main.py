from turtle import Screen, Terminator
from .snake import Snake
from .food import Food
from .scoreboard import Scoreboard
import time

def play_snake():
    screen = Screen()
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    def quit_game():
        nonlocal game_on
        game_on = False

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(quit_game, "q")

    game_on = True
    while game_on:
        try:
            screen.update()
            time.sleep(0.1)
            snake.move()

            # Detect collision with food
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            # Detect collision with wall
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                scoreboard.reset()
                snake.reset()

            # Detect collision with tail
            for seg in snake.segments[1:]:
                if snake.head.distance(seg) < 10:
                    scoreboard.reset
                    snake.reset()
                    
        except Terminator:
            game_on = False

    screen.update()
    print("Game stopped. Returning to menu...")
    time.sleep(2)
    screen.bye()