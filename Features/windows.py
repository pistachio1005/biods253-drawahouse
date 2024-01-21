import turtle as t

 #Draw square window
def rectangle(custom_turtle, width, height):
    for _ in range(2):
        custom_turtle.forward(width)  #Move and turn turtle
        custom_turtle.right(90)       
        custom_turtle.forward(height)
        custom_turtle.right(90)     

def draw_window(x,y,width,height):
    t.color("blue")

    #Move the second turtle to a new position
    t.penup()
    t.goto(x,y)  #Move 200 spaces to the right
    t.pendown()

    #Draw rectangular door
    rectangle(t, width, height)

def main():
    t.speed("fastest")
    draw_window(0,0,50,50)
    # Hide Turtle
    t.hideturtle()

    # Keep the window open
    t.done()

if __name__ == "__main__":
    main()
