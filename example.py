# Import all from ASCIIGraphics
from ASCIIGraphics import *

# Initialisation function.
init()
# Starts the keyboard listener
# Clears the terminal


# class that inherits from the Box class
class Jumper(Box):
    def __init__(self, size=(10, 10), pos=(5, 20), fill='rounded box'):
        super().__init__(size, pos, fill)
        # super calls Boxes __init__() function.
        # Only size is a required argument
        # pos, fill, and custom_pattern have default values but can be changed here

        # more variables for logic
        self.jumping = False
        self.yvel = 0
        self.xvel = 0
        self.maxxvel = 3

    # add an update function to make changes
    def update(self):
        # self.move changes self.pos by the given x and y
        # down is positive
        self.move(self.xvel, -self.yvel)
        self.yvel -= 1


        # game logic
        if not ("left" in pressed_keys or "right" in pressed_keys):
            if self.xvel > 0:
                self.xvel -= 1
            if self.xvel < 0:
                self.xvel += 1

        if self.xvel > self.maxxvel:
            self.xvel = self.maxxvel
        elif self.xvel < -self.maxxvel:
            self.xvel = -self.maxxvel
        

        # self.collide returns true if there positions are overlapping
        if self.collide(ground):
            self.jumping = False
            self.yvel = 0
            while self.collide(ground):
                self.move(0, -1)
            self.move(0, 2)

        # checking self.collide(screen) is an easy way to see if we are offscreen
        if not self.collide(screen):
            self.pos = (20, 0)

        # pressed_keys is a set of all currently pressed keys
        if "up" in pressed_keys and not self.jumping:
            self.jumping = True
            self.yvel = 6
        if "left" in pressed_keys:
            self.xvel -= 1
        if "right" in pressed_keys:
            self.xvel += 1
        if "down" in pressed_keys:
            if self.yvel > 0:
                self.yvel = 0
            self.xvel = 0





# screen and ground are both Boxes
screen = Box((150, 30), fill="rounded box")
ground = Box((150, 20), pos=(0, 28), fill="rounded box")
jumper = Jumper()

run = True
while run:
    # end condition
    if "esc" in pressed_keys:
        run =False

    # call update method
    jumper.update()

    # combine grounds plate with screens and set that equal to screen.face (used when printing)
    # this resets the drawing
    screen.draw(ground)

    # adds jumpers plate to screen.face
    # unlike draw() does not reset
    screen.draw_next(jumper)

    # to display the screen simply print it
    print(screen)

    # wait the amount of time necessary to run at 15 FPS
    tick(15)

# stops keyboard listening and calls quit()
qquit()

