from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", move=False, align='left', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

