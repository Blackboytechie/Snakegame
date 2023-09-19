from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r_x = randint(-280, 280)
        r_y = randint(-280, 280)
        self.goto(r_x, r_y)



