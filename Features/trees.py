import turtle as t

def draw_tree(x, y, trunk_height, trunk_width, foliage_diameter):
    """
    Draws a simple tree with a trunk and foliage.
    Arguments:
    x, y: The position of the base of the trunk
    trunk_height: The height of the trunk
    trunk_width: The width of the trunk
    foliage_diameter: The diameter of the foliage
    """

    # Draw the trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(trunk_width)
        t.left(90)
        t.forward(trunk_height)
        t.left(90)
    t.end_fill()

    # Draw the foliage
    t.penup()
    t.goto(x - foliage_diameter//2 +65, y + trunk_height - foliage_diameter//2 + 50)
    t.pendown()
    t.color("forestgreen")
    t.begin_fill()
    t.circle(foliage_diameter//1.5)
    t.end_fill()

def draw_filled_rectangle(x, y, width, height, color):
    """
    Function to draw a filled rectangle.
    Arguments:
    x, y: starting position
    width, height: dimensions of the rectangle
    color: fill color of the rectangle
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color, color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

