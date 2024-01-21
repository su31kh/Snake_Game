import turtle
from turtle import Turtle,Screen
import random
MOVE_DIST = 20

class Snake:
    def __init__(self):
        self.all_tuts = []
        self.create_snake(5)
        # self.all_tuts[3].color = "green"
        self.head = self.all_tuts[0]

    def add_part(self):
        i = 0
        tmp = Turtle(shape="square")
        # tmp.color("darkorchid1")
        turtle.colormode(255)
        tmp.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        tmp.penup()
        tmp.goto(x=i * (-20), y=0)
        i += 1
        self.all_tuts.append(tmp)

    def create_snake(self, x):
        for i in range(x):
            self.add_part()


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):

            for num in range(len(self.all_tuts) - 1, 0, -1):
                x = self.all_tuts[num - 1].xcor()
                y = self.all_tuts[num - 1].ycor()
                self.all_tuts[num].goto(x, y)
            self.head.forward(MOVE_DIST)
            # self.all_tuts[0].right(90)