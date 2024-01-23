import turtle as t

def filled_circle(radius, color):
    """
    Helper function to draw a filled circle
    """
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def rectangle(custom_turtle, width, height):
    for _ in range(2):
        custom_turtle.forward(width)
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)     

