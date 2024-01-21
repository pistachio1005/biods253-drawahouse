import turtle as t
from Features.outline import *
from Features.clouds import *

def main():
    t.speed(10)

    # Set up Turtle and set canvas dimensions
    t.setup(width=1000, height=1000)


    # Draw the house outline
    draw_house(-200, -150, 400, 200, 100)
    # Draw the clouds
    draw_cloud(-300,300,40)
    draw_cloud(250,250,30)

    # Hide Turtle
    t.hideturtle()

    # Keep the window open
    t.done()

if __name__ == "__main__":
    main()
