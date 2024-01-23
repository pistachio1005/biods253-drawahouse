import turtle as t

def rectangle(custom_turtle, width, height):
    """
    Helper function to draw a rectangle
    """
    for _ in range(2):
        custom_turtle.forward(width)
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)     

def draw_door(x,y,width,height,color):
    """
    Function to draw the entrance door
    """

    t.color(color)
    t.begin_fill()

    #door position
    t.penup()
    t.goto(x,y)
    t.pendown()

    rectangle(t, width, height)
    t.end_fill()
