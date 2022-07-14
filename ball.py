from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x = 0
        self.y = 0
        self.x_dist = 50
        self.y_dist = 50
        # self.speed(1)

    def move(self):
        if self.ycor() >= 400:
            self.y_dist = -50

        if self.ycor() <= -400:
            self.y_dist = 50

        if self.xcor() >= 700:
            pass

        self.goto(x=self.x, y=self.y)

        self.x += self.x_dist
        self.y += self.y_dist
        print(self.xcor(), self.ycor())
