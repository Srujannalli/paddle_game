from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class score_a(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-200, 270)
        self.write(f"scoreboard : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score_a(self):
        self.clear()
        self.score += 1
        self.write(f"scoreboard : {self.score}", align='center', font=FONT)

class score_b(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(200, 270)
        self.write(f"scoreboard : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score_b(self):
        self.clear()
        self.score += 1
        self.write(f"scoreboard : {self.score}", align='center', font=FONT)