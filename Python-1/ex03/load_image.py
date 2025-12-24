from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads the image path prints the dimension/shape
    of the image and returns the values of each pixel"""
    try:
        assert type(path) is str, "Type is not a string"
        img = Image.open(path)
        imgArray = np.array(img)
        print("The shape of image is:", imgArray.shape)
        return imgArray
    except (FileNotFoundError, PermissionError) as error:
        print(error)
    except AssertionError as error:
        print("AssertionError:", error)

    return None
