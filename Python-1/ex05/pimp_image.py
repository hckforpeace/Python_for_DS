import numpy as np
from PIL import Image


def displayImage(img: np.array):
    IMG = Image.fromarray(img)
    IMG.show()


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    array = array.copy()
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            array[i, j, 0] = 255 - array[i, j, 0]
            array[i, j, 1] = 255 - array[i, j, 1]
            array[i, j, 2] = 255 - array[i, j, 2]
    displayImage(array)
    return array


def ft_red(array) -> np.array:
    """keep the R in RGB of the image received."""
    array = array.copy()
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            array[i, j, 1] = 0
            array[i, j, 2] = 0
    displayImage(array)
    return array


#
def ft_green(array) -> np.array:
    """keep the G in RGB of the image received."""
    array = array.copy()
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            array[i, j, 0] = 0
            array[i, j, 2] = 0
    displayImage(array)
    return array


def ft_blue(array) -> np.array:
    """keep the B in RGB of the image received."""
    array = array.copy()
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            array[i, j, 0] = 0
            array[i, j, 1] = 0
    displayImage(array)
    return array


def ft_grey(array) -> np.array:
    """Image becomes black and white"""
    array = array.copy()
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            gray = (
                0.299 * array[i, j, 0] + 0.587 * array[i, j, 1]
                + 0.114 * array[i, j, 2]
            )
            array[i, j, 0] = gray
            array[i, j, 1] = gray
            array[i, j, 2] = gray
    displayImage(array)
    return array


# img = ft_load("landscape.jpg")
# inverted = ft_grey(img)
# IMG = Image.fromarray(inverted)
# IMG.show()
