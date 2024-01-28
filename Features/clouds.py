import turtle as t
from shapes import *

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