import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates the Body Mass Index
    of out of the height and weight"""
    assert len(height) == len(weight), "lists are not the same size"
    harr = np.array(height)
    warr = np.array(weight)
    bmi = warr / (harr**2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if the list of bmi's is
    above the limit and make a list of bool out of the result"""
    nbmi = np.array(bmi)
    bmiLimit = nbmi > limit
    return bmiLimit.tolist()
