import turtle as t

def draw_house(x, y, width, height, roof_height):
    """
    Function to draw the outline of the home
    Argument: 
    (x,y): starting position
    width: width of the house
    height: height of the house(rectangular part)
    roof_height: height of the roof(triangle part)
    """

    # Draw rectangle (base of the house)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)

    # Move to the starting position for the roof
    t.penup()
    t.goto(x, y + height)
    t.pendown()

    # Draw triangle (roof of the house)
    t.goto(x + width / 2, y + height + roof_height)
    t.goto(x + width, y + height)
    t.goto(x, y + height)
