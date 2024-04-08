from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules =cythonize("cython2_1.pyx"))
