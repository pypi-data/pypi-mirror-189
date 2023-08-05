# Intro

Primawera is a simple imager viewer with support for non-standard image data such as complex, floating point
or 3D image data.

# Installation

Very soon it will be possible to install it using pip. Right now you have to build it yourself.

# Building

## Required packages

More detailed information about version of packages is inside the `pyproject.toml` file.

- Python 3.10
- numpy
- PIL
- PyQt5
- Qt
- h5py

## Building and installing the package

Make sure you have the latest version of `setuptools`, `pip` and `venv` packages as the building requires some
newer features of `setuptools`.

Inside the root folder run:
```bash
python -m build
```

The command should build a wheel file inside the `dist` folder. To install it run:
```bash
pip install <PATH TO WHEEL FILE>
```

# Usage

## Run empty window

It is possible to run the viewer without any data.
```python
from primawera.app import create_window
create_window()
```

## Visualise numpy data

If you want to visualise data inside a numpy array, you will have to import the function `run_app`. You also have to
specify the bitdepth (for floating point data provide any nonzero number) and the mode (see [https://pillow.readthedocs.io/en/stable/handbook/concepts.html](Pillow image modes)).
```python
from primawera.app import run_app
run_app(data, bitdepth, mode)
```

## Run from terminal

Simply run
```bash
primawera
```
