import turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # head is defined after creating
        self.head = self.segments[0]

    # create the snake body
    def create_snake(self):
        """Creates a snake body"""
        self.segments = []
        j = 0
        for i in range(3):
            part = turtle.Turtle(shape='square')
            self.segments.append(part)
            part.color('white')
            part.penup()
            part.goto(x=j, y=0)
            j -= 20

    def head_up(self):
        """Turns the snake upwards"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def head_down(self):
        """Turns the snake downwards"""
        if self.head.heading() != 90:
            self.head.setheading(-90)

    def head_left(self):
        """Turns the snake to our left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def head_right(self):
        """Turns the snake to our right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        """Function to move the snake continuously"""
        for i in range(len(self.segments) - 1, 0, -1):
            a, b = self.segments[i - 1].pos()
            self.segments[i].goto(a, b)
        self.head.forward(20)

    def check_wall_collision(self):
        """Checks if the snake head is colliding with any of the walls of the screen"""
        head = self.head
        if head.xcor() > 290 or head.ycor() > 290 or head.xcor() < -290 or head.ycor() < -290:
            return True
        return False

    def grow_snake(self):
        """Adds another segment to the snake once it eats the food"""
        part = turtle.Turtle(shape='square')
        # this should be done before append
        a, b = self.segments[len(self.segments) - 1].pos()
        part.goto(a, b)
        self.segments.append(part)
        part.penup()
        part.color('white')

    def detect_tail_collision(self):
        """Checks for any collision with tail"""
        # doesn't check dist with head itself and the 1st seg(cuz it's connected)
        for i in range(1, len(self.segments)-1):
            if self.head.distance(self.segments[i]) < 10:
                return True
        return False

    def reset_snake(self):
        """Clears the screen by removing snake"""
        for i in self.segments:
            i.hideturtle()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
