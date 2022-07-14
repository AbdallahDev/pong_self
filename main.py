from turtle import Screen
import time

from ball import Ball
from board import Board
from net import Net
from scoreboard import ScoreBoard

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
BOARD2_UP_KEY = 'i'
BOARD2_DOWN_KEY = 'k'
BALL_DISTANCE = 80

screen = Screen()
screen.setup(width=TABLE_WIDTH, height=TABLE_HEIGHT)
screen.bgcolor(TABLE_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)
screen.listen()

net = Net()
scoreboard1 = ScoreBoard(x=-50)
scoreboard2 = ScoreBoard(x=50)
board1 = Board(x=-BOARD_XCOR, y=BOARD_YCOR)
board2 = Board(x=BOARD_XCOR, y=-BOARD_YCOR)


def game():
    ball = Ball()

    while True:
        screen.onkey(fun=board1.up, key=BOARD1_UP_KEY)
        screen.onkey(fun=board1.down, key=BOARD1_DOWN_KEY)

        screen.onkey(fun=board2.up, key=BOARD2_UP_KEY)
        screen.onkey(fun=board2.down, key=BOARD2_DOWN_KEY)

        if ball.distance(board2) < BALL_DISTANCE:
            if ball.y_dist == 50 or ball.y_dist == -50:
                ball.x_dist = -50

        if ball.distance(board1) < BALL_DISTANCE:
            if ball.y_dist == -50 or ball.y_dist == 50:
                ball.x_dist = 50

        ball.move()

        if ball.xcor() < -750:
            scoreboard2.increase_score()
            break
        if ball.xcor() > 750:
            scoreboard1.increase_score()
            break

        screen.update()
        time.sleep(0.45)


while True:
    game()
