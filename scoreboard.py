from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("high_score.txt", "r") as f:
            self.high_points = int(f.read())
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update_points()

    def update_points(self):
        self.goto(-250, 250)
        self.write(f"Score : {self.points}", move=False, align="center", font=("arial", 10, "normal"))
        self.goto(-160, 250)
        self.write(f"High Score : {self.high_points}", move=False, align="center", font=("arial", 10, "normal"))

    def game_over(self):
        if self.points > self.high_points:
            self.high_points = self.points
        with open("high_score.txt","w") as f:
            f.write(f"{self.high_points}")
        self.points = 0
        self.clear()
        self.update_points()

    def track_points(self):
        self.points += 1
        self.clear()
        self.update_points()
