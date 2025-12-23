from load_image import ft_load 
from PIL import Image
import numpy as np

def zoom(img: np.array) -> np.array:
    beginX = int(img.shape[0] * 0.30)
    beginY = int(img.shape[1] * 0.30)
    endX = img.shape[0] - beginX
    endY = img.shape[1] - beginY


    sliced = img[beginX:endX, beginY:endY,]
    # sliced = img
    print("Image shape:", sliced.shape )
    Img = Image.fromarray(sliced)
    Img.show()
    return np.array(Img)


zoom(ft_load("animal.jpeg"))
