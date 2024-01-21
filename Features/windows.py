import turtle

 #Draw square window
def square_window(my_turtle):
    for _ in range(4):
        my_turtle.forward(50)  #Move the turtle 50 spaces
        my_turtle.right(90)    #Turn the turtle

#Create a turtle graphics screen
window = turtle.Screen()

#Create the first turtle
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("blue")

square_window(turtle1)

#Create the second turtle
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("blue")

#Move the second turtle to a new position
turtle2.penup()
turtle2.goto(200, 0)  #Move 200 spaces to the right
turtle2.pendown()

square_window(turtle2)

#Close the turtle graphics window when clicked
window.exitonclick()
