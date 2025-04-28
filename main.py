import random
import turtle
from http.cookiejar import user_domain_match
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
cherepahi =[]
user_bet = screen.textinput("Make your bet", "Which cherepaha will win the gonka? Enter a color(red, yellow, green, cyan, blue, magenta): ")


is_race_on = False
x = -230
y = -100
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.setpos(x, y)
    y += 40
    cherepahi.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for cherepaha in cherepahi:
        if cherepaha.xcor() > 230:
            winner = cherepaha.color()[0]
            if winner == user_bet:
                print(f"You win! {winner} is fastest one!")
            else:
                print(f"You lose. {winner} is fastest one.")
            is_race_on = False

        random_distance = random.randint(0, 10)
        cherepaha.forward(random_distance)

screen.exitonclick()