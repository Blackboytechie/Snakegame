from turtle import Screen, Turtle
from random import choice
import time

seg = []
dir = [0.0, 90.0, 180.0, 270.0]


class Snake():
    def __init__(self):
        self.new_seg = None
        self.pos = [(0, 0), (-20, 0), (-40, 0)]
        self.seg = []
        self.color = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
        self.snakebody()

    def check_body_collision(self):
        for x in self.seg[1:len(self.seg) - 1]:
            if self.seg[0].distance(x) < 10:
                return True

    def snakebody(self):
        for pos in self.pos:
            self.new_seg = Turtle("square")
            self.new_seg.speed("fastest")
            self.new_seg.color(choice(self.color))
            self.new_seg.penup()
            self.new_seg.goto(pos)
            self.seg.append(self.new_seg)

    def snake_grow(self):
        g_x = self.seg[2].xcor()
        g_y = self.seg[2].ycor()
        self.new_seg = Turtle("square")
        self.new_seg.color(choice(self.color))
        self.new_seg.penup()
        self.new_seg.goto(g_x, g_y)
        self.seg.append(self.new_seg)

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            n_x = self.seg[i - 1].xcor()
            n_y = self.seg[i - 1].ycor()
            self.seg[i].goto(n_x, n_y)
        print("moving")
        self.seg[0].forward(20)

    def up(self):
        if self.seg[0].heading() != dir[3]:
            self.seg[0].seth(90)

    def right(self):
        if self.seg[0].heading() != dir[2]:
            self.seg[0].seth(0)

    def left(self):
        if self.seg[0].heading() != dir[0]:
            self.seg[0].seth(180)

    def down(self):
        if self.seg[0].heading() != dir[1]:
            self.seg[0].seth(270)

    def refresh_snake(self):
        for i in range(0, len(self.seg)):
            self.seg[i].goto(1000, 1000)
        self.seg.clear()
        self.snakebody()
