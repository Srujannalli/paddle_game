from turtle import Turtle
GAME_BORDER = -380


class Objects(Turtle):
    def __init__(self):
        super().__init__()

    def paddle1(self):
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1, 1)
        self.penup()
        self.goto(GAME_BORDER, 0)

    def up(self):
        Y_coordinate = self.ycor()
        Y_coordinate += 30
        self.goto(GAME_BORDER, Y_coordinate)

    def down(self):
        Y_coordinate = self.ycor()
        Y_coordinate -= 30
        self.goto(GAME_BORDER, Y_coordinate)

