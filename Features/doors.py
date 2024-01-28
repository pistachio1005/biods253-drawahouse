import turtle as t
from shapes import *

def draw_door(x,y,width,height,color):
    """
    Function to draw the entrance door
    Arguments:
    (x,y): starting position
    width: width of the door
    height: height of the door
    color: color of the door
    """

    t.color(color)
    t.begin_fill()

    #door position
    t.penup()
    t.goto(x,y)
    t.pendown()

    rectangle(t, width, height)
    t.end_fill()
