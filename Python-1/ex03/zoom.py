from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np


def zoom(img: np.array) -> None:
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

    Img = Image.fromarray(sliced)
    # convert to grayscale
    grayscale_img = ImageOps.grayscale(Img)

    print(
        "New shape after slicing:",
        np.array(grayscale_img)[:, :, np.newaxis].shape,
        "or",
        np.array(grayscale_img).shape,
    )
    print(np.array(grayscale_img)[:, :, np.newaxis])

    plt.imshow(grayscale_img, cmap="gray")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    img = ft_load("animal.jpeg")
    if img is not None:
        zoom(img)
