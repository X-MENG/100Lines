from vec import *

WIDTH = 600
HEIGHT = 440

BACK_COLOR = (0, 0, 0)

rcH = 240
rcW = 5

SRC_COLOR = (200, 0, 100)
DEST_COLOR = (10, 100, 200)

class MyRect:
    def __init__(self, x, y, clr):
        self.pos = Vec2(x, y)
        self.clr = clr

    def Draw(self):
        rc = Rect((self.pos.x, self.pos.y), (rcW, rcH))
        screen.draw.filled_rect(rc, self.clr)

curX = 50
curY = 100

rc_list = []
p = 0
pspd = 0.01
rc_step = rcW
enable_lerp = True

def lerp_color(src_color, dest_color):
    global curX, p, rc_list, enable_lerp

    if p > 1.0:
        p = 1.0
        enable_lerp = False

    cur_color = [0, 0, 0]

    for i in range(0, 3):
        cur_color[i] = src_color[i] * (1 - p) + dest_color[i] * p

    rc_list.append(MyRect(curX, curY, tuple(cur_color)))
    curX += rc_step
    p += pspd

def update():
    if enable_lerp == False:
        return

    lerp_color(SRC_COLOR, DEST_COLOR)

def draw():
    screen.clear()
    screen.fill(BACK_COLOR)
    for rc in rc_list:
        rc.Draw()
