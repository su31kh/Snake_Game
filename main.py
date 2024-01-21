from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# tim = Turtle()


# tim.shape("square")
# tim.penup()
# tim.color("pink")
# all_tuts = []
# all_tuts.append(tim)

screen.listen()
snake = Snake()
snake.head.color("pink")
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
   # time.sleep(1 / (10))
    time.sleep(10/(100+scoreboard.score))
    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()
        scoreboard.gain_score()
        snake.add_part()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300:
        # game_on = False
        # scoreboard.game_over()
        xx = snake.head.xcor()
        xx = xx*(-1)
        yy = snake.head.ycor()
        snake.head.goto(x=xx,y=yy)

    if snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_on = False
        # scoreboard.game_over()
        xx = snake.head.xcor()
        yy = snake.head.ycor()
        yy = yy * (-1)
        snake.head.goto(x=xx, y=yy)


    for tuts in snake.all_tuts[1:]:
        if snake.head.distance(tuts) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()