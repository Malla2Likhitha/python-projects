import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from divider import Divider

# screen setup
screen = turtle.Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# divider
divide = Divider()

# scoreboard setup
l_score = ScoreBoard(-100, 'LEFT')
r_score = ScoreBoard(100, 'RIGHT')

# 2 sliders - create and move
slider_r = Paddle(350)
slider_l = Paddle(-350)

screen.listen()
# should listen to the respective if pong is on the respective side
screen.onkeypress(slider_r.up, 'Up')
screen.onkeypress(slider_r.down, 'Down')
screen.onkeypress(slider_l.up, 'w')
screen.onkeypress(slider_l.down, 's')

# create a pong and make it move
pong = Ball()
speed = 0.1


def game_on(score_l, score_r, k):
    """While the score < 10, game goes on"""
    factor = 1

    game = True
    while game:
        screen.update()
        time.sleep(k)
        pong.move()

        # pong wall top bottom collision - bounce
        pong.updown_collision()

        # pong slider collision - bounce
        # double collision with the slider???  -> solved  # 350 - 10 = 340,
        # again -20 --> so that the ball doesn't seem to go inside the paddle, therefore 340 - 20 = 320
        # back slider hit  --> solved  # 350 + 10 = 360
        if ((pong.distance(slider_r) < 50 and 360 > pong.xcor() > 320) or
                (pong.distance(slider_l) < 50 and -360 < pong.xcor() < -320)):
            pong.slider_collision()
            # increase the pace every collision
            k *= 0.9  # always positive

        # pong wall side collision - game over, score to the opponent
        if pong.out() is not None:
            if pong.out():
                factor *= -1
                score_l.increase_score()
                if score_l.game_over():
                    return
            else:
                score_r.increase_score()
                if score_r.game_over():
                    return

            game = False

    slider_r.goto(350, 0)
    slider_l.goto(-350, 0)
    pong.reset_pos(factor)
    # pong.setheading(45)
    # game - start again after updating score
    game_on(score_l, score_r, k)


game_on(l_score, r_score, speed)

turtle.mainloop()
