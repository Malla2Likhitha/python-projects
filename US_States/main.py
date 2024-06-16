import turtle
import pandas
import answer
import scoreboard

screen = turtle.Screen()
screen.setup(height=491, width=725)
screen.bgpic('blank_states_img.gif')

ans = answer.Answer()
score = scoreboard.ScoreBoard()

states_data = pandas.read_csv('50_states.csv')

guessed = []
while not score.done():
    guess = screen.textinput('US States Game', 'Enter the name of the state: ').lower()
    if guess == 'exit':
        to_learn = [i for i in states_data.state if i not in guessed]
        df = pandas.DataFrame(to_learn)
        df.to_csv('yet_to_learn.csv')
        break
    else:
        for s in states_data.state:
            if s.lower() == guess and s not in guessed:
                guessed.append(s)
                # req_data = states_data[states_data['state'] == s]
                # ans.fill(s, int(req_data.x.iloc[0]), int(req_data.y.iloc[0]))
                req_data = states_data[states_data['state'] == s].to_numpy()
                ans.fill(s, req_data[0][1], req_data[0][2])
                score.score += 1
                score.update_score()

turtle.mainloop()

# give up button
# timer
