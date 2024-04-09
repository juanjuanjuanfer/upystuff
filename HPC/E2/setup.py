from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("kmeans_cython.pyx"),  # Pass 'annotate=True' here
)