import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):

    def __init__(self, level):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(300, random.randint(-250, 250))
        self.move_dist = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT
        self.cars = []

    def move(self):
        self.goto(self.xcor() - self.move_dist, self.ycor())

    def increase_speed(self):
        self.move_dist += MOVE_INCREMENT

    def done(self):
        return self.xcor() < -280

