from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.go_up = 0
        self.go_down = 0
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(350, 0)


def go_up(self):
    new_y = self.paddle.ycor() + 20
    self.paddle.goto(self.paddle.xcor(), new_y)


def go_down(self):
    new_y = self.paddle.ycor() - 20
    self.paddle.goto(self.paddle.xcor(), new_y)
