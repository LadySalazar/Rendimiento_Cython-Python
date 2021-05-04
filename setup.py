from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts = (cythonize('Cy_functionE.pyx'))

setup(ext_modules=exts,include_dirs=[numpy.get_include()])