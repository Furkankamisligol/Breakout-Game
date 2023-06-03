from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Live(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.goto(position)
        self.live = 3

    def write_live(self):
        self.write(str(self.live), align=ALIGNMENT, font=FONT)
