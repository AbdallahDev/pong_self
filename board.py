from turtle import Turtle, Screen

MOVEMENT_DISTANCE = 50


class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.setposition(x=x, y=y)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(to_angle=90)

    def up(self):
        if self.ycor() <= 400:
            self.forward(MOVEMENT_DISTANCE)

    def down(self):
        if self.ycor() >= -400:
            self.backward(MOVEMENT_DISTANCE)
