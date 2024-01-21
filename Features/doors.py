import turtle as t

#draw rectangluar door
def rectangle(custom_turtle, width, height):
    for _ in range(2):
        custom_turtle.forward(width)  #Move and turn turtle
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)     

def draw_door(x,y,width,height):
    """
    Function to draw the entrance door
    """

    t.color("brown")
    t.begin_fill()

    #door position
    t.penup()
    t.goto(x,y)  #Adjust door position
    t.pendown()

    #Draw rectangular door
    rectangle(t, width, height)
    t.end_fill()

def draw_gdoor(x,y,width,height):
    """
    Function to draw the garage door
    """
    t.begin_fill()
    t.color("gray")

    #Position the first garage turtle without drawing
    t.penup()
    t.goto(x, y)  # Adjust the position as needed
    t.pendown()

    #draw first rectangular garage
    rectangle(t, width, height)
    t.end_fill()

