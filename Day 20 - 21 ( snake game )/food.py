from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("lavender")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.goto(random_x, random_y)
