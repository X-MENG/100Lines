from microbit import *
import random

p = [2, 2]
ghost = [0, 0]
def move_pixel(d):
    global p
    display.set_pixel(p[0], p[1], 0)
    p[0] += d[0]
    p[1] += d[1]
    if p[0] >= 5:
        p[0] = 4
    elif p[0] < 0:
        p[0] = 0
    if p[1] >= 5:
        p[1] = 4
    elif p[1] < 0:
        p[1] = 0
    display.set_pixel(p[0], p[1], 9)
    
    if ghost == p:
        # audio.play(Sound.HAPPY)
        update_ghost()
    sleep(300)

def update_ghost():
    global p, ghost
    while True:
        gx = random.randint(0, 4)
        gy = random.randint(0, 4)
        if [gx, gy] != p:
            break
    
    ghost[0] = gx
    ghost[1] = gy
    display.set_pixel(gx, gy, 4)

move_pixel(p)
update_ghost()

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if x < -100:
        move_pixel((-1, 0))
    elif x > 100:
        move_pixel((1, 0))

    if y < -100:
        move_pixel((0, -1))
    elif y > 100:
        move_pixel((0, 1))
        
        
