import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self, x_pos, name):

        super().__init__()
        self.color('white')
        self.penup()
        self.goto(x_pos, 210)
        self.score = 0
        self.update_score()
        self.hideturtle()
        self.name = name

    def update_score(self):
        """Updates the score"""
        self.clear()
        self.write(self.score, font=("Arial", 51, "normal"), align='center')

    def increase_score(self):
        """Increases the score by 1"""
        self.score += 1
        self.update_score()
        
    def game_over(self):
        """Checks if the game is over where one of them scores 10"""
        if self.score == 10:
            self.goto(0, 0)
            self.write(f'{self.name} player is the winner', font=("Arial", 21, "normal"), align='center')
            return True
