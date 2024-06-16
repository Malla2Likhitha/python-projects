import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-310, 200)
        with open('highscore.txt') as data:
            self.highscore = int(data.read())
        self.update_score()

    def update_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as data:
                data.write(str(self.highscore))
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.highscore}', font=('Arial', 12, 'normal'))

    def done(self):
        if self.score == 50:
            self.clear()
            self.goto(0, 0)
            self.write('Yay!! You guessed all the 50 states of the US', align='center', font=('Arial', 20, 'normal'))
            return True
        return False
