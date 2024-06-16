import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.make_food()

    def make_food(self):
        """Creates new food object at a random location on the screen"""
        r_ht = random.randint(-280, 280)
        r_wd = random.randint(-280, 280)
        self.goto(r_wd, r_ht)

    def food_collision(self, head):
        """Checks if the snake reaches the food and if yes, creates another food object"""
        if head.distance(self) < 15:
            self.make_food()
            return True
        return False

    # def clear_food(self):
    #     self.hideturtle()
