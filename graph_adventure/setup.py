from distutils.core import setup
from Cython.Build import cythonize

setup(name='Graph utils',
      ext_modules=cythonize("utils.pyx"))