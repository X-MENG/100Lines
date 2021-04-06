from microbit import *
import time
import utime
class Cursor:
    def __init__(self, r, c):
        self.cells = {}
        self.update(r, c)

    def update(self, r, c):
        self.cells['mid'] = [r, c]
        self.cells['up'] = None
        self.cells['down'] = None
        self.cells['left'] = None
        self.cells['right'] = None
        if r - 1 >= 0:
            self.cells['up'] = [r - 1, c]
        if r + 1 < 5:
            self.cells['down'] = [r + 1, c]
        if c - 1 >= 0:
            self.cells['left'] = [r, c - 1]
        if c + 1 < 5:
            self.cells['right'] = [r, c + 1]

board = [[0 for c in range(5)] for r in range(5)]
cur = Cursor(2, 2)
blink = 1

def draw_board():
    for r in range(5):
        for c in range(5):
            display.set_pixel(r, c, board[r][c] * 3)
                
def draw_cursor():
    if blink == 0:
        draw_board()
    else:
        for v in cur.cells.values():
            if v != None:
                display.set_pixel(v[0], v[1], 5)
        
def confirm():
    update_board(cur)
    for row in board:
        if 0 in row:
            draw_board()
            break
    else:
        global is_vectory
        is_vectory = True
        display.clear()
        display.show(Image.HAPPY)

def v_move():
    mid_row = cur.cells['mid'][0] + 1
    mid_col = cur.cells['mid'][1]
    if mid_row >= 5:
        mid_row = 0
    cur.update(mid_row, mid_col)
    draw_board()
    
def h_move():
    mid_row = cur.cells['mid'][0]
    mid_col = cur.cells['mid'][1] + 1
    if mid_col >= 5:
        mid_col = 0
    cur.update(mid_row, mid_col)
    draw_board()

def flip_cell(r, c):
    global board
    board[r][c] = not board[r][c]

def update_board(cur):
    for v in cur.cells.values():
        if v != None:
            flip_cell(v[0], v[1])

draw_board()
last_time = 0
last_flash_time = 0
a_pressed = False
b_pressed = False
is_vectory = False

while True:
    if pin_logo.is_touched():
        board = [[0 for c in range(5)] for r in range(5)]
        cur = Cursor(2, 2)
        is_vectory = False
        draw_board()
    if is_vectory == True:
        continue
    if button_a.was_pressed():
        a_pressed = True
        if b_pressed == False:
            last_time = time.ticks_ms()
    if button_b.was_pressed():
        b_pressed = True
        if a_pressed == False:
            last_time = time.ticks_ms()
    if time.ticks_ms() - last_time > 200:
        last_time = time.ticks_ms()
        if a_pressed == True and b_pressed == True:
            confirm()
        elif a_pressed == True:
            blink = 1
            v_move()
            draw_cursor()
        elif b_pressed == True:
            blink = 1
            h_move()
            draw_cursor()
        a_pressed = False
        b_pressed = False
    if time.ticks_ms() - last_flash_time > 1000:
        draw_cursor()
        last_flash_time = time.ticks_ms()
        blink = not blink
