# ASCIIGraphics

This is a python program I wrote that can display stuff in the terminal. This is also my first github thing. 

Curreantly it only works in windows. 

# How To Use

## Setup
The following steps are a suggestion only. 

1. Find the file called `ASCIIGraphics.py` and put it in the same folder as your project.
2. At the top of your code type `import ASCIIGraphics as graphics`. This will give you access to all the functionality in `ASCIIGraphics.py`
3. Ensure you have numpy and pynput installed. `ASCIIGraphics.py` needs these to run.
     - Use `pip install numpy` and `pip install pynput`
     - See [here](https://packaging.python.org/en/latest/tutorials/installing-packages/) for more information.
4. You can test to see if `ASCIIGraphics.py` is working by typing `graphics.test()` in your code.
     - See `example.py` for an example of this.
6. This code can only be run in specific places. For exampe, WindowsPowershell is fine, but the default IDLE that comes with python is not. This may require some trial and error and likely depends on your computer. For me, opening Powershell and running the comand `python [path to file]` works.
7. After running the test code a screen with a large box will appear. A smaller box is in the top left corner. Use arrow keys to move and escape to quit. If the screen doesn't appear to be rendering properly, press escape, put the output terminal in fullscreen, and run it again.
8. Congragulations, you have completed setup!!!
   
