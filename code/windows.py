import turtle as t
from shapes import *


def draw_window(x,y,width,height):
    """
    Function to draw a window
    Arguments:
    (x,y): starting position
    width: width of the window
    height: height of the window
    """
    t.color("blue")

    #Move the second turtle to a new position
    t.penup()
    t.goto(x,y)  #Move 200 spaces to the right
    t.pendown()

    #Draw rectangular door
    rectangle(t, width, height)