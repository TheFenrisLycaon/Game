'''Conway's Game Of Life
Game-Of-Life Rules:
 1.
 Any live cell with fewer than two live neighbours
 dies, as if caused by under-population.
 2.
 Any live cell with two or three live neighbours lives
 on to the next generation.
 3.
 Any live cell with more than three live neighbours
 dies, as if by over-population.
 4.
 Any dead cell with exactly three live neighbours be-
 comes a live cell, as if by reproduction.
 '''

from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
import random
import sys
import numpy as np
from matplotlib import use as mpluse

mpluse('TkAgg')
choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size):
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas):
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas):
    canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(canvas.shape[0]))
    for r, row in enumerate(canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, canvas[r - 1:r + 2, c - 1:c + 2])
    canvas = next_gen_canvas
    del next_gen_canvas
    return canvas.tolist()


def __judge_point(pt, neighbours):
    dead = 0
    alive = 0
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1
    if pt:
        alive -= 1
    else:
        dead -= 1
    state = pt
    if pt:
        if alive < 2:
            state = False
        elif alive == 2 or alive == 3:
            state = True
        elif alive > 3:
            state = False
    else:
        if alive == 3:
            state = True
    return state


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception(usage_doc)
    canvas_size = 640
    c = create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap(['w', 'k'])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        pass
