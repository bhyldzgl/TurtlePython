import turtle

drawing_board = turtle.Screen() #Ekran oluşturuyoruz
drawing_board.bgcolor("green") #screnn regini yeşil olarak ayarladık
drawing_board.title("Python Turtle") #ekranın title ismini belirlerdik

'''
turtle_instance = turtle.Turtle() #
turtle_instance.forward(100)
turtle_instance2 = turtle.Turtle()
turtle_instance2.left(45)
turtle_instance2.forward(100)
'''
#square
turtle_instance = turtle.Turtle()
'''

turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
Bu şekilde de yapabiliriz ama döngü ile ded yapılabilir.
'''

for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)

turtle.done()