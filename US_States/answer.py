import turtle


class Answer(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def fill(self, state, x, y):
        self.goto(x, y)
        self.write(state, align='center')
