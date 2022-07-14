from line import Line


def create_net():
    y = -500
    for _ in range(20):
        line = Line(y=y)
        y += 50


class Net:
    def __init__(self):
        create_net()
