import turtle
import random

from setuptools.sandbox import hide_setuptools

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle Game")
FONT = ('Arial',30,'normal')
GRID_SIZE = 10
score = 0
game_over = False
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10]


#turtle list
turtle_list = []

#countdown turtle
countdownTurtle = turtle.Turtle()

def countdown(time) :
    global game_over
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark blue")
    countdownTurtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdownTurtle.setposition(0, y - 30)
    countdownTurtle.clear()

    if time > 0 :
        countdownTurtle.clear()
        countdownTurtle.write(arg="Time : {} ".format(time) , move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time-1) , 1000)
    else :
        game_over = True
        countdownTurtle.clear()
        hide_turtle()
        countdownTurtle.write(arg="Game Over ! ", move=False, align="center", font=FONT)

#score turtle
score_turtle = turtle.Turtle()
def setup_score_turtle() :
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() /2
    y = top_height * 0.8
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score 0",move=False,align="center",font=FONT)

def make_turtle(x,y) :
    def handle_click(x, y) :
        global score
        score = score + 1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(score),move=False,align="center",font=FONT)

    t = turtle.Turtle()
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*GRID_SIZE, y*GRID_SIZE)
    turtle_list.append(t)




def setup_turtles():
    for x in x_coordinates :
        for y in y_coordinates :
            make_turtle(x,y)

def hide_turtle():
    for t in turtle_list:
        t.hideturtle()
#recursive
def show_turtles_randomly() :
    if not game_over :
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtle()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)


start_game_up()

turtle.mainloop()