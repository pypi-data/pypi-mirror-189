import numpy as np
from numpy.typing import ArrayLike


# Expects an array with dtype=float
def linear_stretch(array: ArrayLike) -> ArrayLike:
    frames, height, width = array.shape
    max_val, min_val = np.max(array), np.min(array)
    if max_val - min_val == 0:
        print("Error: Cannot apply linear stretch filter on constant images, "
              "which would cause a division by 0 error! Ignoring filter.")
        return array
    factor = 1.0 / (max_val - min_val)
    for n in range(frames):
        array[n] = array[n] - min_val
        array[n] = array[n] * factor
    return array


def gamma_correction(array: ArrayLike, factor: float) -> ArrayLike:
    max_value = array.max()
    array /= max_value
    array **= factor
    return array * max_value


def linear_contrast(array: ArrayLike, factor: float) -> ArrayLike:
    return array * factor


def logarithm_stretch(array: ArrayLike, factor=1.0) -> ArrayLike:
    if array.min() < 0:
        # Shifting if the array contains negative numbers.
        array += abs(array.min())
    return factor * np.log(array + 1.0)
