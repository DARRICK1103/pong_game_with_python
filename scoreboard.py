from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 258)
        self.write(self.l_score, align="center", font=("Courier", 20, "bold"))

        self.goto(100, 258)
        self.write(self.r_score, align="center", font=("Courier", 20, "bold"))

        self.goto(0, 258)
        self.write("Score", align="center", font=("Courier", 20, "bold"))

    def add_l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_r_point(self):
        self.r_score += 1
        self.update_scoreboard()