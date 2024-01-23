import turtle as t
from features.outline import *
from features.clouds import *
from features.trees import *
from features.windows import *
from features.doors import *

def main():
    t.speed("fastest")

    # Set up Turtle and set canvas dimensions
    canvas_width = 1000
    canvas_height = 1000
    t.setup(canvas_width, canvas_height)

    # Draw the yard
    yard_start_x = -500
    yard_start_y = -500
    yard_width = canvas_width
    yard_height = 300
    yard_color = "green"
    draw_yard(yard_start_x, yard_start_y, yard_width, yard_height, yard_color)

    # Draw the house outline
    house_width = 400
    house_height = 200
    roof_height = 100   
    house_start_x = - house_width/2
    house_start_y = -150
    draw_house(house_start_x, house_start_y, house_width, house_height, roof_height)

    # Draw the clouds (2*clouds)
    cloud_start_x1 = -300
    cloud_start_y1 = 300
    cloud_size_1 = 40
    cloud_start_x2 = 250
    cloud_start_y2 = 250
    cloud_size_2 = 30
    draw_cloud(cloud_start_x1, cloud_start_y1, cloud_size_1)
    draw_cloud(cloud_start_x2, cloud_start_y2, cloud_size_2)

    # Draw trees
    tree_start_x1 = -400
    tree_start_y1 = -200
    trunk_height = 100
    trunk_width = 40
    foliage_diameter = 120
    tree_start_x2 = 300
    tree_start_y2 = -200
    draw_tree(tree_start_x1, tree_start_y1, trunk_height, trunk_width, foliage_diameter)
    draw_tree(tree_start_x2, tree_start_y2, trunk_height, trunk_width, foliage_diameter)
    
    # Draw door
    door_width = 40
    door_height = 80
    door_color = "brown"
    door_start_x = -door_width/2
    door_start_y = -70
    draw_door(door_start_x, door_start_y, door_width, door_height, door_color)

    # Draw garage doors
    gdoor_start_x1 = -190
    gdoor_start_x2 = 140
    gdoor_start_y = -50
    gdoor_width = 50
    gdoor_height = 100
    gdoor_color = "grey"   
    draw_door(gdoor_start_x1, gdoor_start_y, gdoor_width, gdoor_height, gdoor_color)
    draw_door(gdoor_start_x2, gdoor_start_y, gdoor_width, gdoor_height, gdoor_color)

    # Draw windows
    window_start_x1 = -190
    window_start_x2 = -105
    window_start_x3 = 55
    window_start_x4 = 140
    window_start_y = 10
    window_width = 50
    window_height = 50
    draw_window(window_start_x1, window_start_y, window_width, window_height)
    draw_window(window_start_x2, window_start_y, window_width, window_height)
    draw_window(window_start_x3, window_start_y, window_width, window_height)
    draw_window(window_start_x4, window_start_y, window_width, window_height)

    # Hide Turtle
    t.hideturtle()

    # Keep the window open
    t.done()

if __name__ == "__main__":
    main()
