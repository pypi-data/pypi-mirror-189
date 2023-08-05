from os import listdir, path
from os.path import isdir, isfile
from typing import Tuple

import h5py
import numpy as np
from PIL import Image
from numpy.typing import ArrayLike


def tiff_to_array(image) -> ArrayLike:
    """
    Takes a Tiff image and returns the raw data as a numpy array.
    :param image: Tiff image (PIL).
    :return: Numpy array with data.
    """
    result = []
    for i in range(image.n_frames):
        image.seek(i)
        current_frame = np.array(image)
        result.append(current_frame)
    return np.array(result)


def load_data(data_path: str) -> Tuple[ArrayLike, int, str]:
    """
    Takes a path to a file or a folder and tries to load the image data.
    :param data_path: Path to data.
    :return: A tuple of the data as a numpy array, bitdepth and mode of the
             image.
    """
    if isdir(data_path):
        raw_data, bitdepth, mode = load_folder(data_path)
    elif isfile(data_path):
        raw_data, bitdepth, mode = load_file(data_path)
    else:
        raise RuntimeError(
            f"'{data_path}' is neither a regular file nor a directory!")
    return raw_data, bitdepth, mode


def load_folder(path_to_dir: str):
    raw_data = []
    bitdepth = -1
    mode = ""
    for file in listdir(path_to_dir):
        if file.endswith(".png"):
            file_data, file_bitdepth, file_mode = load_file(
                path.join(path_to_dir, file))

            # Check if files are compatible
            if bitdepth != -1 and bitdepth != file_bitdepth:
                print(
                    f"[Error] Not all images in the directory '{path_to_dir}'\
                      have the same bitdepth!")
                return raw_data, bitdepth, mode

            if mode != "" and mode != file_mode:
                print(
                    f"[Error] Not all images in the directory '{path_to_dir}'\
                     have the same color mode!")
                return raw_data, bitdepth, mode

            # If this is the first file, set the bitdepth accordingly
            if bitdepth == -1:
                bitdepth = file_bitdepth
            if mode == "":
                mode = file_mode

            raw_data.append(file_data[0])
    return np.array(raw_data), bitdepth, mode


def load_file(file_path: str):
    bitdepth = -1
    # TODO: decompose this if else
    if file_path.endswith((".tif", ".tiff")):
        with Image.open(file_path) as tiff_file:
            mode = tiff_file.mode
            raw_data = tiff_to_array(tiff_file)
    elif file_path.endswith(".h5"):
        with h5py.File(file_path) as h5_file:
            h5_dataset = h5_file["Image"]
            type = h5_dataset.dtype
            # TODO: properly rework this
            if type in [np.float64, np.double, np.float32, np.float16,
                        np.single]:
                mode = "F"
                bitdepth = 16
            elif type == np.complex128:
                mode = "C"
                bitdepth = 16
            else:
                mode = "L"
            raw_data = np.zeros(h5_dataset.shape, dtype=type)
            h5_dataset.read_direct(raw_data)
    elif file_path.endswith((".jpg", ".png")):
        with Image.open(file_path) as image_file:
            raw_data = np.array(image_file, dtype=np.uint8).copy()
            mode = image_file.mode
    else:
        raise NotImplementedError(f"Unsupported file format!")

    if mode == "I;16" or mode == "I;16B":
        bitdepth = 16
        mode = "grayscale"
    elif mode == "L":
        bitdepth = 8
        mode = "grayscale"
    elif mode == "RGB":
        bitdepth = 8
        mode = "rgb"
    elif mode == "1":
        bitdepth = 1
    elif mode == "F" or mode == "C":
        # TODO: this is prob. wrong. Floating point imgs. in h5 can have
        #       other bitdepths.
        bitdepth = 8  # According to PIL docs
        assert bitdepth != -1
    else:
        raise NotImplementedError(f"Mode: \"{mode}\" is not"
                                  "implemented.")

    # grayscale single frame data
    if len(raw_data.shape) == 2 or mode == "rgb":
        raw_data = np.array([raw_data])

    return raw_data, bitdepth, mode
