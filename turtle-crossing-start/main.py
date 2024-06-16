import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the turtle
tur = Player()
# scoreboard
level = Scoreboard()
# cars
cars = []

screen.listen()
# screen.onkey(tur.move(), 'Space') -- no brackets for the function and no caps for s in space
screen.onkeypress(tur.move, 'space')

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if count % 5 == 0:
        car = CarManager(level.level)
        cars.append(car)

    for car in cars:
        car.move()
        if car.done():
            cars.remove(car)
            car.hideturtle()

    if tur.finish():
        # increase the score
        level.increase_level()
        for i in cars:
            # prev cars speed increase, new cars' speed will anyway increase while the instance is being made
            i.increase_speed()

    for i in cars:
        if tur.distance(i) < 20:  #  or tur.distance(i) < 30 and abs(tur.ycor() - i.ycor()) < 20
            print(tur.ycor())
            print(tur.xcor())
            print(tur.distance(i))
            print(i.ycor())
            print(i.xcor())
            game_is_on = False
            level.game_over()

    count += 1

turtle.mainloop()

