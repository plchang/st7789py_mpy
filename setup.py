from setuptools import setup, find_packages

setup(
    name='st7789py_mpy',
    version='0.1',
    packages=find_packages(),
    package_dir={'st7789py_mpy'},
    entry_points={ 'console_scripts': ['st7789py_mpy =__main__:main' ] }
)
