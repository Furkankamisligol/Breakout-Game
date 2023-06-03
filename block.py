from turtle import Turtle


class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 3)
        self.pu()
        self.goto(position)
        self.seth(0)

