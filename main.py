from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet" , "Which turtle is going to win the race ? Enter your color: ")
color = ["red", "green", "blue", "yellow", "purple", "orange"]
y_cord = [80,50,20,-10,-40,-70]
all = []

for turtles in range(0, 6):

    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color[turtles])
    new_turtle.goto(-230, y_cord[turtles])
    all.append(new_turtle)

rase_on = False

if user_bet:
    rase_on = True

while rase_on:

    for turtle in all:
        if turtle.xcor() > 200:
            race_on = False
            wining = turtle.pencolor()
            if wining == user_bet:
               print(f"You`ve won ! The {wining} is winner.")
            else:
               print(f"You`ve lost ! The {wining} is winner.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
