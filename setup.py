from distutils.core import setup

setup(
    description='Desktop markdown editing software with live preview',
    author='Logan Mortimer',
    author_email='last.karrde@gmail.com',
    name='deskmarkdown',
    version='0.1',
    py_modules=['deskmarkdown'],
    install_requires=['markdown2','PySide'],
    )