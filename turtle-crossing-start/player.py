import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() < 280:
            self.goto(0, self.ycor() + MOVE_DISTANCE)

    def finish(self):
        if self.ycor() < 280:
            return False
        self.goto(STARTING_POSITION)
        return True


