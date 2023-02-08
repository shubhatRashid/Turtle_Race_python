from turtle import Turtle , Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

j = -100
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i - 1])
    new_turtle.penup()
    new_turtle.goto(-240, j)
    j += 33
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won, the color of winning turtle is {winning_color}")
            else:
                print(f"you have lost, the color of winning turtle is {winning_color}")

        speed = random.randint(1, 10)
        turtle.forward(speed)








screen.exitonclick()