from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.start_and_angle()

    def move(self):
        self.fd(1)

    def start_and_angle(self):
        self.goto(0, 0)
        k = random.randint(45, 135)
        angles = []
        angles.append(k)
        a = random.choice(angles)
        self.seth(a)


"""
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -self.y_move
        
        
"""
    