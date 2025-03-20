import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Drawing Shirinking Square")

turtle_instance = turtle.Turtle()

def shrinkingSquare(size) :
    for i in range(4) :
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

shrinkingSquare(200)
shrinkingSquare(180)
shrinkingSquare(160)
shrinkingSquare(140)
shrinkingSquare(120)
shrinkingSquare(100)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)


turtle.done()