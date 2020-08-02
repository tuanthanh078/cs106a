"""
File: babygraphics.py
---------------------
This program builds a powerful visualization of the data contained in
the dictionary name_data.
The dictionary is formed as {name : {year : rank}}
"""

import tkinter
import babynames
import babygraphicsgui as gui


# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    return GRAPH_MARGIN_SIZE + year_index * (width-2*GRAPH_MARGIN_SIZE)/(len(YEARS))

def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the baby name,
    returns the y coordinate of the data point described the rank
    of the baby name associated with that year. If rank is MAX_RANK,
    the y coordinate should be equal to the y coordinate of the bottom
    horizontal line.

    Input:
        height (int): The height of the canvas
        rank (int): The rank of the baby name
    Returns:
        y_coordinate (float): The y coordinate of the data point described
        the rank of the baby name associated with that year
    >>> round(get_y_coordinate(600, 1), 1)
    20.0
    >>> round(get_y_coordinate(600, 1000), 1)
    580.0
    >>> round(get_y_coordinate(600, 11), 1)
    25.6
    """
    if rank == MAX_RANK:
        return height*1.0 - GRAPH_MARGIN_SIZE
    else:
        return (height-2*GRAPH_MARGIN_SIZE)/(MAX_RANK-1) * (rank-1) + GRAPH_MARGIN_SIZE

def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width-2*GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, height-GRAPH_MARGIN_SIZE, width-2*GRAPH_MARGIN_SIZE, height-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, 0, x, height)
        canvas.create_text(x+TEXT_DX, height-GRAPH_MARGIN_SIZE+TEXT_DX, text=str(YEARS[i]), anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    color_index = 0
    data_points = []
    for name in lookup_names:
        data_points = []
        ranks = name_data[name]
        for i in range(len(YEARS)):
            x = get_x_coordinate(width, i)
            y = 0
            if YEARS[i] in ranks:
                rank = ranks[YEARS[i]]
                y = get_y_coordinate(height, rank)
                canvas.create_text(x+TEXT_DX, y-TEXT_DX,
                                   text=name+' '+str(rank),
                                   fill=COLORS[color_index%len(COLORS)],
                                   anchor=tkinter.SW)
            else:
                y = get_y_coordinate(height, MAX_RANK)
                canvas.create_text(x + TEXT_DX, y - TEXT_DX,
                                   text=name + ' *',
                                   fill=COLORS[color_index % len(COLORS)],
                                   anchor=tkinter.SW)
            data_points.append((x, y))
        for i in range(len(data_points)-1):
            canvas.create_line(data_points[i][0], data_points[i][1], data_points[i+1][0], data_points[i+1][1],
                               width=LINE_WIDTH, fill=COLORS[color_index%len(COLORS)])
        color_index += 1

# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
