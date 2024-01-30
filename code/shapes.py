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
    """
    Helper function to draw a rectangle
    """
    for _ in range(2):
        custom_turtle.forward(width)
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)     

# import turtle
# from PIL import Image

# # def filled_circle(radius, color):
# #     """
# #     Helper function to draw a filled circle
# #     """
# #     t = turtle.Turtle()
# #     t.color(color, color)
# #     t.begin_fill()
# #     t.circle(radius)
# #     t.end_fill()
# #     t.hideturtle()

#     # # Save the drawing to a PostScript file
#     # canvas = turtle.getcanvas()
#     # canvas.postscript(file="drawing.ps", colormode='color')

#     # # Convert the PostScript file to PNG
#     # with Image.open("drawing.ps") as img:
#     #     img.save("drawing.png")

# # Example usage
# filled_circle(50, 'red')


