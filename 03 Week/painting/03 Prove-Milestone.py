# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 4, scene_width, scene_height, width=0, fill="midnight blue")
    draw_stars(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    pass

def draw_stars(canvas, scene_width, scene_height):
    stars = random.randrange(100,300,3)
    while stars >= 0:
        if stars == 0:
            break
        else:
            stars -= 1
            x = random.randrange(0, scene_width)
            x2 = x-1
            y = random.randrange(0, scene_height)
            y2 = y-1
            draw_oval(canvas,x,y,x2,y2,width=1, outline="white",)
    pass

def draw_clouds(canvas, scene_width, scene_height):
    clouds = random.randrange(25,75,3)
    while clouds >= 0:
        if clouds == 0:
            break
        else:
            clouds -= 1
            x = random.randrange(0, scene_width)
            cloud_size = random.randrange(25,100,5)
            cloud_height = round(scene_height*10/13,)
            y = random.randrange(cloud_height, scene_height)
            y2 = y+cloud_size
            x2 = x+8+cloud_size
            draw_oval(canvas,x,y,x2,y2,fill="snow3", outline="snow3",)
    pass

def draw_ground(canvas, scene_width, scene_height):
    ground = scene_height / 4
    draw_rectangle(canvas, 0, 0, scene_width, ground, width=0, fill="green")
    draw_house(canvas, scene_width, scene_height)
    pass

def draw_house(canvas, scene_width, scene_height):
    ground = round(scene_height / 4)
    center_x = random.randrange(0,scene_width)
    center_y = random.randrange(0,ground)
    left_x = center_x - 25
    left_y = center_y - 20
    right_x = center_x + 25
    right_y = center_y + 10
    draw_rectangle(canvas, left_x, left_y, right_x, right_y, width=0, fill="red")
    left_bottom_x = center_x + 40
    right_bottom_x = center_x - 40
    height = center_y + random.randrange(25,50)
    draw_polygon(canvas, left_bottom_x, center_y, right_bottom_x, center_y, center_x, height, fill="white")
    pass

# Call the main function so that
# this program will start executing.
main()