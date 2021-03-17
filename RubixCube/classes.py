from itertools import cycle
import os
import sys


class Utils:
    def __init__(self):
        pass

    def clear():
        """ Clearing the screen """

        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def banner():
        """ Printing banner """

        print("  _ \        |    _)                 __|        |          ")
        print("    /  |  |   _ \  | \ \ / \ \ /    (     |  |   _ \   -_) ")
        print(" _|_\ \_,_| _.__/ _|  _\_\  _\_\   \___| \_,_| _.__/ \___| ")
        print()

    def showMoves(l, n):
        l.reverse()
        # print(l)
        if n == -1:
            n = len(l)
        elif n == 0:
            return
        # print(n)
        for i in range(n):
            if l[i] != None:
                print(l[i])
            else:
                n -= 1


class face:

    def __init__(self, color):
        """ Generating face of the cube """
        self.color = color
        k = color[0].upper()
        self.right = face
        self.up = face
        self.down = face
        self.state = [[k, k, k]]*3

    def showFace(self):
        """ showing face """
        self.printEdge(0, 0)
        self.printEdge(1, 0)
        self.printEdge(2, 0)

    def printEdge(self, n, f):

        if f == 0:
            for i in range(3):
                print(self.state[n][i], end='  |  ') if i < 2 else print(
                    self.state[n][i])
        elif f == 1:
            print(" "*16, end='')
            for i in range(3):
                print(self.state[n][i], end='  |  ') if i < 2 else print(
                    self.state[n][i])
        elif f == 2:
            for i in range(3):
                print(self.state[n][i], end='  |  ') if i < 2 else print(
                    self.state[n][i], end='\t')


class rubixx:

    def __init__(self):
        self.red = face('red')
        self.blue = face('blue')
        self.green = face('green')
        self.white = face('white')
        self.orange = face('orange')
        self.yellow = face('yellow')
        self.link()

    def link(self):
        self.red.right = self.blue
        self.red.left = self.green
        self.red.up = self.white
        self.red.down = self.yellow

        self.blue.right = self.orange
        self.blue.left = self.red
        self.blue.up = self.white
        self.blue.down = self.yellow

        self.orange.right = self.green
        self.orange.left = self.blue
        self.orange.up = self.white
        self.orange.down = self.yellow

        self.green.right = self.red
        self.green.left = self.orange
        self.green.up = self.white
        self.green.down = self.yellow

        self.white.right = self.blue
        self.white.left = self.green
        self.white.up = self.orange
        self.white.down = self.red

        self.yellow.right = self.blue
        self.yellow.left = self.green
        self.yellow.down = self.orange
        self.yellow.up = self.red

        self.red.opp = self.orange
        self.orange.opp = self.red
        self.blue.opp = self.green
        self.green.opp = self.blue
        self.white.opp = self.yellow
        self.yellow.opp = self.white

        self.current = self.red

    def showCube(self):

        # print upper face
        self.current.up.printEdge(0, 1)
        self.current.up.printEdge(1, 1)
        self.current.up.printEdge(2, 1)

        print()

        # print four adjacent faces

        self.current.left.printEdge(0, 2)
        self.current.printEdge(0, 2)
        self.current.right.printEdge(0, 2)
        self.current.opp.printEdge(0, 0)
        self.current.left.printEdge(1, 2)
        self.current.printEdge(1, 2)
        self.current.right.printEdge(1, 2)
        self.current.opp.printEdge(1, 0)
        self.current.left.printEdge(2, 2)
        self.current.printEdge(2, 2)
        self.current.right.printEdge(2, 2)
        self.current.opp.printEdge(2, 0)

        print()

        # print lower face

        self.current.down.printEdge(0, 1)
        self.current.down.printEdge(1, 1)
        self.current.down.printEdge(2, 1)

    def turnCube(self):
        res = 'Turned the cube '
        dir = int(input(
            "\n\t[1] Right\t\t[2] Left\n\t[3] Up\t\t\t[4] Down\n\t[0] See opposite face.\n\nEnter Direction::\t"))
        res += 'right\n'*(dir == 1) + 'left\n'*(dir == 2) + 'upwards\n'*(dir == 3) + \
            'downwards\n'*(dir == 4) + 'to face opposite face\n'*(dir == 0)
        if dir == 0:
            # self.current.left.showFace()
            temp = self.current.left
        elif dir == 1:
            # self.current.right.showFace()
            temp = self.current.right
        elif dir == 2:
            # self.current.left.showFace()
            temp = self.current.left
        elif dir == 3:
            # self.current.up.showFace()
            temp = self.current.up
        elif dir == 4:
            # self.current.down.showFace()
            temp = self.current.down
        else:
            print("Invalid Input. Try again.")
            self.turnCube()

        ask = int(input("\n\t[0] Set default\t\t[1] Go Back\n\nEnter::"))
        if ask == 0:
            self.current = temp
        elif ask == 1:
            pass
        else:
            print("Invalid Input. Try again.")
            self.turnCube()

        if ask == 0:
            return res

    def showState(self):
        self.current.showFace()

    def getDirection(self):
        res = 'Rotated '
        x = int(
            input("\n\t\t[1] Up\t\t[2] Down\n\t\t[3] Left\t[4] Right\n\t\t[5]Move current face\n\nEnter Side::"))
        res += 'upper edge '*(x == 1) + 'lower edge '*(x == 2) + 'left edge ' * \
            (x == 3) + 'right edge '*(x == 4) + 'current face '*(x == 5)

        if x == 1 or x == 2:
            y = int(
                input("\n\t\t[1] Left\t\t[2] Right\n\nEnter Direction::\t"))
            res += 'to the left\n'*(y == 1) + 'to the right\n'*(y == 2)
        elif x == 3 or x == 4:
            y = int(
                input("\n\t\t[1] Upwards\t\t[2] Downwards\n\nEnter Direction::\t"))
            res += 'upwards\n'*(y == 1) + 'downwards\n'*(y == 2)
        elif x == 5:
            y = int(
                input("\n\t\t[1] Anti-ClockWise\t\t[2] ClockWise\n\nEnter Direction::\t"))
            res += 'Anti-ClockWise\n'*(y == 1) + 'ClockWise'*(y == 2)
        else:
            print("Invalid Input\n")
            self.getDirection()

        self.rotate(x, y)
        return res

    def rotate(self, side, direc):
        print(side, direc)

        if side == 1:
            if direc == 1:
                self.current.state[0], self.current.right.state[0], self.current.opp.state[0], self.current.left.state[
                    0] = self.current.right.state[0], self.current.opp.state[0], self.current.left.state[0], self.current.state[0]
            elif direc == 2:
                self.current.right.state[0], self.current.opp.state[0], self.current.left.state[0], self.current.state[0] = self.current.state[0], self.current.right.state[0], self.current.opp.state[0], self.current.left.state[
                    0]

        elif side == 2:
            if direc == 1:
                self.current.state[2], self.current.right.state[2], self.current.opp.state[2], self.current.left.state[
                    2] = self.current.right.state[2], self.current.opp.state[2], self.current.left.state[2], self.current.state[2]
            elif direc == 2:
                self.current.right.state[2], self.current.opp.state[2], self.current.left.state[2], self.current.state[2] = self.current.state[2], self.current.right.state[2], self.current.opp.state[2], self.current.left.state[
                    2]

        elif side == 3:
            if direc == 1:
                for i in range(0, 3):
                    self.current.state[i][0], self.current.up.state[i][0], self.current.opp.state[i][0], self.current.down.state[i][
                        0] = self.current.up.state[i][0], self.current.opp.state[i][0], self.current.down.state[i][0], self.current.state[i][0]
            if direc == 2:
                for i in range(0, 3):
                    self.current.up.state[i][0], self.current.opp.state[i][0], self.current.down.state[i][0], self.current.state[i][
                        0] = self.current.state[i][0], self.current.up.state[i][0], self.current.opp.state[i][0], self.current.down.state[i][0]

        elif side == 4:
            if direc == 1:
                for i in range(0, 3):
                    self.current.state[i][2], self.current.up.state[i][2], self.current.opp.state[i][2], self.current.down.state[i][
                        2] = self.current.up.state[i][2], self.current.opp.state[i][2], self.current.down.state[i][2], self.current.state[i][2]
            if direc == 2:
                for i in range(0, 3):
                    self.current.up.state[i][2], self.current.opp.state[i][2], self.current.down.state[i][2], self.current.state[i][
                        2] = self.current.state[i][2], self.current.up.state[i][2], self.current.opp.state[i][2], self.current.down.state[i][2]

        elif side == 5:
            if direc == 1:
                for r in self.current.state:
                    r.reverse()

                for i in range(3):
                    for j in range(i):
                        self.current.state[i][j], self.current.state[j][i] = self.current.state[j][i], self.current.state[i][j]

            elif direc == 2:
                for r in self.current.state:
                    r.reverse()
                for i in range(3):
                    for j in range(i):
                        self.current.state[j][i], self.current.state[i][j] = self.current.state[i][j], self.current.state[j][i]
