from turtle import Turtle


class Line(Turtle):
    def __init__(self, y):
        super().__init__()
        self.y = y
        self.penup()
        self.color('white')
        self.setposition(x=0, y=self.y)
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=0.5)
