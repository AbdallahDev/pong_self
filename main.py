from turtle import Screen, Turtle

from board import Board

TABLE_COLOR = "black"
GAME_TITLE = "Pong Game"
TABLE_WIDTH = 1500
TABLE_HEIGHT = 1000
TABLE_TOP_EDGE = TABLE_HEIGHT / 2
TABLE_LEFT_EDGE = -(TABLE_WIDTH / 2)

screen = Screen()
screen.setup(width=TABLE_WIDTH, height=TABLE_HEIGHT)
screen.bgcolor(TABLE_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)
screen.listen()

y = -500
for _ in range(20):
    net = Turtle()
    net.penup()
    net.color("white")
    net.setposition(x=0, y=y)
    net.shape('square')
    net.shapesize(stretch_wid=1, stretch_len=0.5)
    y += 50

board1 = Board(x=-700, y=400)
board2 = Board(x=700, y=-400)

while True:
    screen.onkey(fun=board1.up, key="w")
    screen.onkey(fun=board1.down, key="s")

    screen.onkey(fun=board2.up, key="Up")
    screen.onkey(fun=board2.down, key="Down")

    screen.update()

screen.exitonclick()
