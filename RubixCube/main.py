#!/home/fenris/anaconda3/bin/python
from classes import rubixx as cube
from classes import Utils as u

if __name__ == '__main__':
    x = cube()
    moves = []
    # x.current.showFace()
    # x.rotate(1, 2)
    # print(x.current.state
    while True:
        temp = []
        c = int(input(
            "Main Menu\n\n\t[1] Turn Cube\t\t[2] Show Cube\n\t[3] Show State\t\t[4] Rotate\n\t[5] Show Moves\n\n\t[0] Exit\n\nEnter::\t"))
        u.clear()
        u.banner()
        if c == 0:
            u.clear()
            exit()
        elif c == 1:
            temp = x.turnCube()
        elif c == 2:
            x.showCube()
        elif c == 3:
            x.showState()
        elif c == 4:
            temp = x.getDirection()
        elif c == 5:
            u.showMoves(moves, int(
                input("Enter number of moves to show ([0] Exit\t[-1] All)::\t")))
        else:
            print("Invalid Choice. Try again.")
        moves.append(temp)
