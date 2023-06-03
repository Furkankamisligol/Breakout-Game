from turtle import Turtle, Screen
from ball import Ball
from racket import Racket
from block import Block
from lives import Live
breakout_table = Screen()
breakout_table.setup(width=800, height=600)
breakout_table.title("Breakout")
breakout_table.bgcolor("black")
breakout_table.tracer(0)
Blocks = []

Player_one = Racket((0, -250))

p_ball = Ball()
live_position = (-350, -280)
live_count = Live(live_position)
live_count.write_live()

def blocks():
    for yc in range(3):
        y = 270 - yc*30
        for xc in range(10):
            x = 360 - xc*80
            position = (x, y)
            bloock = Block(position)
            Blocks.append(bloock)




breakout_table.listen()
breakout_table.onkey(fun=Player_one.move_right, key="Left")
breakout_table.onkey(fun=Player_one.move_left, key="Right")

blocks()
game_is_on = True

while game_is_on:
    breakout_table.update()
    p_ball.move()
    if p_ball.ycor() > 290:
        k = p_ball.heading()
        new_k = 360 - k
        p_ball.seth(new_k)
    if p_ball.ycor() < -245:
        if p_ball.distance(Player_one) <= 50:
            k = p_ball.heading()
            new_k = 360-k
            p_ball.seth(new_k)

    elif p_ball.xcor() > 390 or p_ball.xcor() < -390:
        k = p_ball.heading()
        L = k % 90
        m = 90 - L
        n = k + 2 * m
        p_ball.seth(n)

    for block in Blocks:
        if p_ball.ycor() > block.ycor()-5 and p_ball.distance(block) <= 30:
            k = p_ball.heading()
            new_k = 360 - k
            p_ball.seth(new_k)
            block.hideturtle()
            Blocks.pop(Blocks.index(block))

    if p_ball.ycor() < -310:
        live_count.live -= 1
        live_count.clear()
        live_count.write_live()
        if live_count.live == 0:
            game_is_on = False
        else:
            p_ball.start_and_angle()

breakout_table.exitonclick()
