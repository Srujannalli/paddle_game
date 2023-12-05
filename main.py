from scoring import score_a, score_b
from turtle import Turtle, Screen
import time
from paddle1 import Objects
from paddle2 import Paddle2
from ball import Ball
limit = 0.1
screen = Screen()
pd1 = Objects()
pd2 = Paddle2()
balls = Ball()
Score_a = score_a()
Score_b = score_b()
screen.listen()
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)
screen.setup(height=600, width=800)
pd1.speed("slow")
game_on = True
pd1.paddle1()
pd2.paddle2()
screen.onkey(pd1.up, "w")
screen.onkey(pd1.down, "s")
screen.onkey(pd2.go_up, "Up")
screen.onkey(pd2.go_down, "Down")

while game_on:
    time.sleep(limit)
    screen.update()
    balls.move()
    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce()
    if balls.xcor() > 360 and balls.distance(pd2) < 50:
        balls.other_direction()
    if balls.xcor() < -360 and balls.distance(pd1) < 50:
        balls.other_direction()
    if balls.xcor() > 400:
        balls.goto(0, 0)
        balls.move()
        Score_b.increase_score_b()
    if balls.xcor() < -400:
        balls.goto(0, 0)
        balls.move()
        Score_a.increase_score_a()


screen.exitonclick()