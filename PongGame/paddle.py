import turtle


class Paddle(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def up(self):
        """Moves the paddle up"""
        if 240 > self.ycor() >= -240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddle down"""
        if 240 >= self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

