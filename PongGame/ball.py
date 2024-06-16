import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        # self.setheading(45)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball"""
        # self.forward(10)
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def updown_collision(self):
        """The ball bounces if it collides with the upper and lower walls"""
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce()

    def bounce(self):
        """Function to bounce the ball"""
        self.y_move *= -1

    def slider_collision(self):
        """Collision between the ball and slider"""
        self.x_move *= -1

    def out(self):
        """If the ball goes out"""
        if self.xcor() > 390 or self.xcor() < -390:
            return self.xcor() > 0
        return

    def reset_pos(self, factor):
        self.goto(0, 0)
        self.x_move = 10 * factor
        self.y_move = 10

    # def slider_collision(self):
    #     if self.xcor() > 0:
    #         if self.heading() == 45:
    #             self.setheading(135)
    #         else:
    #             self.setheading(225)
    #     else:
    #         if self.heading() == 135:
    #             self.setheading(45)
    #         else:
    #             self.setheading(315)

    # def bounce(self):
    #     if self.heading() == 45:
    #         self.setheading(315)
    #     elif self.heading() == 315:
    #         self.setheading(45)
    #     elif self.heading() == 135:
    #         self.setheading(225)
    #     else:
    #         self.setheading(135)


