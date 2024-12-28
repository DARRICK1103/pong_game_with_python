from turtle import Turtle
PADDLE_MOVE = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)
        self.paddle_move = PADDLE_MOVE
        self.is_moving = False


    def move(self):
        if self.is_moving:
            y = self.ycor()
            if (250 > y > -250
                    or
                    (y > 250 and self.paddle_move < 0)
                    or
                    (y < -250 and self.paddle_move > 0)
            ):
                self.sety(y + self.paddle_move)

    def move_up(self):
        self.is_moving = True
        if self.paddle_move < 0:
            self.paddle_move *= -1


    def move_down(self):
        self.is_moving = True
        if self.paddle_move > 0:
            self.paddle_move *= -1


    def reset(self):
        self.sety(0)
        self.is_moving = False