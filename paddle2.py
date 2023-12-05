from turtle import Turtle
GAME_END = 370


class Paddle2(Turtle):
    def __init__(self):
        super().__init__()

    def paddle2(self):
        self.shape("square")
        self.color("white")
        self.turtlesize(4, 1, 1)
        self.penup()
        self.goto(GAME_END, 0)

    def go_up(self):
        Y_coordinate = self.ycor()
        Y_coordinate += 30
        self.goto(GAME_END, Y_coordinate)

    def go_down(self):
        Y_coordinate = self.ycor()
        Y_coordinate -= 30
        self.goto(GAME_END, Y_coordinate)
