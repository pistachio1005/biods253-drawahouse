import turtle as t
from Features.outline import *
from Features.clouds import *
from Features.trees import *
from Features.windows import *
from Features.doors import *

def main():
    t.speed("fastest")

    # Set up Turtle and set canvas dimensions
    t.setup(width=1000, height=1000)

    # # Draw the yard
    draw_filled_rectangle(-500, -500, 1000, 300, "green")
    # # Draw the house outline
    draw_house(-200, -150, 400, 200, 100)
    # # Draw the clouds
    draw_cloud(-300,300,40)
    draw_cloud(250,250,30)


    # Draw trees
    draw_tree(-400, -200, 100, 40, 120)  # Tree on the left side
    draw_tree(300, -200, 100, 40, 120) 

    # Draw door
    draw_door(-20,-70,40,80)

    # Draw garage doors
    draw_gdoor(-190,-50,50,100)
    draw_gdoor(140,-50,50,100)

    # # Draw windows
    draw_window(-190,10,50,50)
    draw_window(-105,10,50,50)
    draw_window(55,10,50,50)
    draw_window(140,10,50,50)

    # Hide Turtle
    t.hideturtle()

    # Keep the window open
    save_drawing()
    t.done()
    # save_drawing()

from PIL import Image
import io

def save_drawing(filepath = 'full_house.png'):
    canvas = t.getcanvas()
    ps = canvas.postscript(colormode='color')
    
    # Use BytesIO to convert the PostScript data to PNG
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save(filepath, 'png')


if __name__ == "__main__":
    main()