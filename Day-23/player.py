from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_in_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else :
            return False


