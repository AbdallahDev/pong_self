from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.setposition(x=x, y=400)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=self.score, align="center", font=('Cursive', 80, 'normal'))
