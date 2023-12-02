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

# COMMAND TO TEST
# pip install dist\ASCIIGraphics-1.0.0-py3-none-any.whl --force-reinstall
# pip uninstall ASCIIGraphics