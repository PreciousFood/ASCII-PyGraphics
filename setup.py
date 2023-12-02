from setuptools import setup, find_packages


with open("README.md", "r") as file:
    description = file.read()

setup(
    name="ASCIIGraphics", 
    version="1.0.0", 
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pynput"
    ],
    long_description=description,
    long_description_type="text/markdown"

)

# install setup stuffs...
# pip install setuptools wheel twine
# Ensure that it is this structure
# PROJECT_NAME/
# ├── PROJECT_NAME/
# │   ├── __init__.py
# │   └── main.py
# ├── setup.py
# ├── LICENSE.txt
# └── README.md
#
# In __init__.py
#   from .main import [stuff]
# 
# Build stuff
# python setup.py sdist bdist_wheel
#
#
# COMMANDS FOR TESTING (Local)
# pip install dist\ASCIIGraphics-1.0.0-py3-none-any.whl --force-reinstall
# pip uninstall ASCIIGraphics
# pip list
#
#
# Upload time!!!
# twine upload dist/*
# twine upload --repository testpypi dist/*
#
#
# MORE TESTING!
# pip install PROJECT_NAME
