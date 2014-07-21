# setup.py 
from distutils.core import setup
from Cython.Build import cythonize

setup(name = 'ct1',
      ext_modules = cythonize("*.pyx"))
