from turtle import Turtle


class Racket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4)
        self.pu()
        self.goto(position)
        self.seth(0)

    def move_right(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
