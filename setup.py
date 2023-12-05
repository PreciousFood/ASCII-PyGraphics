from setuptools import setup, find_packages

setup(
    name="ASCII-PyGraphics", 
    version="1.0.1", 
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pynput"
    ],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Precious Food",
    author_email="preciousfood84@gmail.com",
    url="https://github.com/PreciousFood/ASCII-PyGraphics"
)


