from setuptools import setup, find_packages

setup(
    name='st7789py_mpy',
    packages=['st7789py_mpy'],
    package_dir={'st7789py_mpy'},
    ...
    entry_points={ 'console_scripts': ['st7789py_mpy =__main__:main' ] }
