"""
File: pyramid.py
----------------
This program draws and displays a pyramid consisting of bricks arranged
in horizontal rows, so that the number of bricks in each row decreases
by one as you move up the pyramid. The pyramid should be centered
at the bottom of the drawing canvas
"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_brick(canvas, x, y, width, height):
    """
    This function  draws a single brick (rectangle) on the graphics canvas.
    The coordinates of brick’s upper left-hand corner are specified by the
    parameters x, y and the brick drawn should be width-pixels wide and
    height-pixels high.
    """
    # Your code goes here
    canvas.create_rectangle(x, y, x+width, y+height)

def draw_brick_row(canvas, x, y, width, height, n):
    """
    This function  draws a row consisting n bricks on the graphics canvas.
    The coordinates of row’s upper left-hand corner are specified by the
    parameters x, y and the brick drawn should be width-pixels wide and
    height-pixels high.
    """
    x_brick = x
    y_brick = y
    for i in range(n):
        draw_brick(canvas, x_brick, y_brick, width, height)
        x_brick += width

def draw_pyramid(canvas):
    """
    This function draws a pyramid consisting of bricks arranged in
    horizontal rows, so that the number of bricks in each row decreases
    by one as you move up the pyramid. The pyramid should be centered
    at the bottom of the drawing canvas
    """
    # Your code goes here
    x_row = (CANVAS_WIDTH - BRICKS_IN_BASE*BRICK_WIDTH)/2
    y_row = CANVAS_HEIGHT - BRICK_HEIGHT
    num_bricks = BRICKS_IN_BASE
    for i in range(BRICKS_IN_BASE):
        draw_brick_row(canvas, x_row, y_row, BRICK_WIDTH, BRICK_HEIGHT, num_bricks)
        x_row += BRICK_WIDTH/2
        y_row -= BRICK_HEIGHT
        num_bricks -= 1


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
