import turtle

#draw rectangluar door
def rectangle(custom_turtle, width, height):
    for _ in range(2):
        custom_turtle.forward(width)  #Move and turn turtle
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)       

#turtle graphics screen
window = turtle.Screen()

#door turtle
door_turtle = turtle.Turtle()
door_turtle.shape("turtle")
door_turtle.color("brown")

#door position
door_turtle.penup()
door_turtle.goto(0, -20)  #Adjust door position
door_turtle.pendown()

#Draw rectangular door
rectangle(door_turtle, 60, 100)

#first garage turtle
garage1_turtle = turtle.Turtle()
garage1_turtle.shape("turtle")
garage1_turtle.color("gray")

#Position the first garage turtle without drawing
garage1_turtle.penup()
garage1_turtle.goto(140, 0)  # Adjust the position as needed
garage1_turtle.pendown()

#draw first rectangular garage
rectangle(garage1_turtle, 100, 120)

#second garage turtle
garage2_turtle = turtle.Turtle()
garage2_turtle.shape("turtle")
garage2_turtle.color("gray")

#position the second garage turtle without drawing
garage2_turtle.penup()
garage2_turtle.goto(-180, 0)  # Adjust the position as needed
garage2_turtle.pendown()

#second rectangular garage
rectangle(garage2_turtle, 100, 120)

#Close the turtle graphics window when clicked
window.exitonclick()
