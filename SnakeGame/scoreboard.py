import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt') as file:
            self.highscore = int(file.read())
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.write(f'Score: 0, High Score: {self.highscore}', font=("Arial", 11, "normal"), align='center')

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.highscore}', font=("Arial", 11, "normal"), align='center')

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f'GAME OVER! Your score is {self.score}.', font=("Arial", 20, "normal"), align='center')

    def reset_score(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f'Score: 0, High Score: {self.highscore}', font=("Arial", 11, "normal"), align='center')
