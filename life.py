import random
import time

ROWS = 50
COLS = 50
CELL_SIZE = 15
HEIGHT = (ROWS * CELL_SIZE)
WIDTH  = (COLS * CELL_SIZE)

BACK_COLOR = (0, 0, 127)
CELL_COLOR = (0, 200, 0)

force = []

def GenCellColor():
    return (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))

def init_map(rows, cols):
    return [[0 for c in range(cols)] for r in range(rows)]

def apply(grid, func):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] = func(r, c)

def clear_map(grid):
    apply(grid, lambda r, c : 0)
    
def draw_cell(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, GenCellColor())
    return 1

def count_neighbors(w, r, c):
    sum = -1 if w[r][c] else 0
    
    for nr in range(r - 1, r + 1 + 1):
        for nc in range(c - 1, c + 1 + 1):
            if nr < 0:
                nr = ROWS - 1
            elif nr >= ROWS:
                nr = 0
            
            if nc < 0:
                nc = COLS - 1
            elif nc >= COLS:
                nc = 0
            if w[nr][nc]:
                sum += 1
 
    return sum

def next_cell(current_world, r, c):
    n = count_neighbors(current_world, r, c)
    if n == 3:
        return 1
    elif n == 2:
        return current_world[r][c]
    else:
        return 0
        
def draw():
    screen.fill(BACK_COLOR)
    apply(world, lambda r, c : (draw_cell(r, c) if world[r][c] else 0))

def random_map(grid):
    apply(grid, lambda r, c : int(random.randint(0, 7) == 0))
            
def update():
    apply(worldNext, lambda r, c : next_cell(world, r, c))
    apply(world, lambda r, c : worldNext[r][c])
    while len(force) > 0:
        n = force.pop()
        world[n[0]][n[1]] = not world[n[0]][n[1]]
    time.sleep(0.5)

def on_mouse_down(pos, button):
    r = pos[1] // CELL_SIZE
    c = pos[0] // CELL_SIZE
    force.append([r, c])

def on_key_down(key, mod, unicode):
    pass

world = init_map(ROWS, COLS)
random_map(world)
worldNext = init_map(ROWS, COLS)