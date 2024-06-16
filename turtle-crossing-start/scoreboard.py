import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)

