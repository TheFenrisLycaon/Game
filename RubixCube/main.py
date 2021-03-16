#!/home/fenris/anaconda3/bin/python
from classes import rubixx as cube
from classes import Utils as u

if __name__ == '__main__':
    x = cube()
    u.clear()
    u.banner()
    # x.showState()
    # x.showCube()
    x.rotate(1, 2)
