import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices the data in intro from start to end
    it will return a part of the initial family list"""

    row1Len = len(family[0])
    assert all(type(row).__name__ == "list" for row in family), "not a list"
    assert all(len(row) == row1Len for row in family), "array not homogeneous"

    fam = np.array(family)
    print("My shape is :", fam.shape)
    newFam = fam[start:end]
    print("My new shape is :", newFam.shape)
    return newFam.tolist()
