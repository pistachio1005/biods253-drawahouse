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

    

    #door position
    t.penup()
    t.goto(x,y)  #Adjust door position
    t.pendown()
    t.color("brown")
    t.begin_fill()
    #Draw rectangular door
    rectangle(t, width, height)
    t.end_fill()

def draw_gdoor(x,y,width,height):
    """
    Function to draw the garage door
    """


    #Position the first garage turtle without drawing
    t.penup()
    t.goto(x, y)  # Adjust the position as needed
    t.pendown()
    t.begin_fill()
    
    t.color("gray")

    #draw first rectangular garage
    rectangle(t, width, height)
    t.end_fill()

