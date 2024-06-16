import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# screen setup
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

# turn the snake
screen.listen()
screen.onkey(snake.head_up, 'Up')
screen.onkey(snake.head_down, 'Down')
screen.onkey(snake.head_left, 'Left')
screen.onkey(snake.head_right, 'Right')

# make food
food = Food()
score = ScoreBoard()

# move the snake
game = True
while game:
    try:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # check collision with wall and tail
        if snake.check_wall_collision() or snake.detect_tail_collision():
            # clear the screen and update
            snake.reset_snake()
            # food.clear_food()
            screen.update()
            score.reset_score()
        # check collision with food and increase score
        if food.food_collision(snake.head):
            score.increase_score()
            snake.grow_snake()

    except turtle.Terminator:
        game = False

turtle.mainloop()
