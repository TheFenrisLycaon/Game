#!/home/fenris/anaconda3/bin/python
from classes import rubixx as cube
from classes import Utils as u

if __name__ == '__main__':
    x = cube()
    # x.current.showFace()
    # x.rotate(1, 2)
    while True:
        c = int(input("Main Menu\n\n\t[1] Turn Cube\t\t[2] Show Cube\n\t[3] Show State\n\n\t[0] Exit\n\nEnter::\t"))
        u.clear()
        u.banner()
        if c == 0:
            exit()
        elif c == 1:
            x.turnCube()
        elif c == 2:
            x.showCube()
        elif c == 3:
            x.showState()
