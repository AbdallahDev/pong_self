from turtle import Screen, Turtle

from board import Board
from net import Net

TABLE_COLOR = "black"
GAME_TITLE = "Pong Game"
TABLE_WIDTH = 1500
TABLE_HEIGHT = 1000
TABLE_TOP_EDGE = TABLE_HEIGHT / 2
TABLE_LEFT_EDGE = -(TABLE_WIDTH / 2)
BOARD_XCOR = 700
BOARD_YCOR = 400
BOARD1_UP_KEY = 'w'
BOARD1_DOWN_KEY = 's'
BOARD2_UP_KEY = 'Up'
BOARD2_DOWN_KEY = 'Down'

screen = Screen()
screen.setup(width=TABLE_WIDTH, height=TABLE_HEIGHT)
screen.bgcolor(TABLE_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)
screen.listen()

net = Net()

board1 = Board(x=-BOARD_XCOR, y=BOARD_YCOR)
board2 = Board(x=BOARD_XCOR, y=-BOARD_YCOR)

while True:
    screen.onkey(fun=board1.up, key=BOARD1_UP_KEY)
    screen.onkey(fun=board1.down, key=BOARD1_DOWN_KEY)

    screen.onkey(fun=board2.up, key=BOARD2_UP_KEY)
    screen.onkey(fun=board2.down, key=BOARD2_DOWN_KEY)

    screen.update()
