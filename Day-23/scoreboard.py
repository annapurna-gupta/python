from turtle import Turtle
FONT = ("Tkinter", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-290, 267)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
