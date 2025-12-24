import numpy as np
from load_image import ft_load
from PIL import Image 

def ft_invert(array) -> np.array:
    print("SHAPE:", array.shape)
    x = array.shape[0]
    y = array.shape[1]

    for i in range(x):
        for j in range(y):
            array[i, j, 0] = 255 - array[i, j, 0]
            array[i, j, 1] = 255 - array[i, j, 1]
            array[i, j, 2] =  255 - array[i, j, 2]
    return array

# def ft_red(array) -> np.array:
#
# def ft_green(array) -> np.array:
#
# def ft_blue(array) -> np.array:
#
# def ft_grey(array) -> np.array:

img = ft_load("landscape.jpg")
inverted = ft_invert(img)
IMG = Image.fromarray(inverted)
IMG.show()
