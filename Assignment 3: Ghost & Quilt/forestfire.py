"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


# Intensity threshold used to determine is a pixel is
# "sufficiently red" to indicate that it is a fire.
INTENSITY_THRESHOLD = 1.05


def highlight_fires(filename):
    """
    This function should highlight the "red" pixels in the image passed in
    and grayscale all other pixels in the image in order to highlight areas
    of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted image with "sufficiently red" pixels highlighted
    """
    image = SimpleImage(filename)
    # Your code to highlight the fires goes here
    for pixel in image:
        if is_sufficiently_red(pixel):
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            color_average = (pixel.red + pixel.green + pixel.blue)//3
            pixel.red = color_average
            pixel.green = color_average
            pixel.blue = color_average
    return image


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    #original_fire.show()
    highlighted_fire.show()

def is_sufficiently_red(pixel):
    return pixel.red >= (pixel.red + pixel.green + pixel.blue)*INTENSITY_THRESHOLD/3

if __name__ == '__main__':
    main()
