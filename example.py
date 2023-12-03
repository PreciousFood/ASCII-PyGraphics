from ASCIIGraphics import *
import math

init()

class Jumper(Box):
    def __init__(self, size = (10, 10), pos=(5, 20), fill='rounded box', custom_pattern=None):
        super().__init__(size, pos, fill, custom_pattern)
        self.jumping = False
        self.yvel = 0
        self.xvel = 0
        self.maxxvel = 3

    def update(self):
        self.move(self.xvel, -self.yvel)
        self.yvel -= 1

        if not ("left" in pressed_keys or "right" in pressed_keys):
            if self.xvel > 0:
                self.xvel -= 1
            if self.xvel < 0:
                self.xvel += 1

        if self.xvel > self.maxxvel:
            self.xvel = self.maxxvel
        elif self.xvel < -self.maxxvel:
            self.xvel = -self.maxxvel
        

        if self.collide(ground):
            self.jumping = False
            self.yvel = 0
            while self.collide(ground):
                self.move(0, -1)
            self.move(0, 2)

        if not self.collide(screen):
            self.pos = (20, 0)


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






screen = Box((150, 30), fill="rounded box")
ground = Box((150, 20), pos=(0, 28), fill="rounded box")
jumper = Jumper()

run = True
while run:
    if "esc" in pressed_keys:
        run =False

    jumper.update()
    screen.draw(ground)
    screen.draw_next(jumper)

    print(screen)

    tick(15)
qquit()

