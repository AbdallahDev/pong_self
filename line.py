from turtle import Turtle

LINE_COLOR = 'white'
LINE_SHAPE = 'square'
LINE_WIDTH = 1
LINE_LENGTH = 0.5


class Line(Turtle):
    def __init__(self, y):
        super().__init__()
        self.y = y
        self.penup()
        self.color(LINE_COLOR)
        self.setposition(x=0, y=self.y)
        self.shape(LINE_SHAPE)
        self.shapesize(stretch_wid=LINE_WIDTH, stretch_len=LINE_LENGTH)
