import turtle


class Divider(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, -300)
        self.hideturtle()
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
