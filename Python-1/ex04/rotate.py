from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np


def grayScaler(img: np.array) -> np.array:
    Img = Image.fromarray(img)
    grayscale_img = ImageOps.grayscale(Img)

    return np.array(grayscale_img)


def zoom(img: np.array) -> np.array:
    """Zooms into the image array and displays image"""
    beginX = int(img.shape[0] * 0.30)
    beginY = int(img.shape[1] * 0.30)
    endX = img.shape[0] - beginX
    endY = img.shape[1] - beginY

    # Zoomed image
    sliced = img[
        beginX:endX,
        beginY:endY,
    ]

    # Img = Image.fromarray(sliced)
    gray = grayScaler(sliced)
    print("The shape of the image is:",
          gray[:, :, np.newaxis].shape, "or", gray.shape)
    print(gray[:, :, np.newaxis])

    return sliced


def transpose(img: np.array) -> np.array:
    """Will transpose the image adn return the array transpose"""
    x = img.shape[0]
    y = img.shape[1]
    z = img.shape[2]

    transposed = np.zeros((y, x, z), dtype=img.dtype)

    for i in range(y):
        for j in range(x):
            transposed[i, j] = img[j, i]

    return transposed


def displayInGrayScale(img: np.array):
    """displays the Image in GrayScale"""
    grayscale_img = grayScaler(img)
    print(
        "New shape after transpose:",
        np.array(grayscale_img)[:, :, np.newaxis].shape,
        "or",
        np.array(grayscale_img).shape,
    )
    print(np.array(grayscale_img))
    plt.imshow(grayscale_img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    img = ft_load("animal.jpeg")
    if img is not None:
        zoomed = zoom(img)
        transposedImg = transpose(zoomed)
        displayInGrayScale(transposedImg)
