import turtle as t


def filled_circle(radius, color):
    """
    Helper function to draw a filled circle
    """
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_cloud(x, y, radius, cloud_color="lightblue"):
    """
    Function to draw a cloud
    Arguments:
    (x,y): starting position
    radius: radius of each filled circle
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

    filled_circle(radius,cloud_color)
    t.forward(radius)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)