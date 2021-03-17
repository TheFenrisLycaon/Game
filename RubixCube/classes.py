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

        self.current.left.printEdge(0,2)
        self.current.printEdge(0,2)
        self.current.right.printEdge(0, 2)
        self.current.opp.printEdge(0,0)
        self.current.left.printEdge(1, 2)
        self.current.printEdge(1, 2)
        self.current.right.printEdge(1, 2)
        self.current.opp.printEdge(1, 0)
        self.current.left.printEdge(2, 2)
        self.current.printEdge(2,2)
        self.current.right.printEdge(2, 2)
        self.current.opp.printEdge(2, 0)

        print()

        # print lower face

        self.current.down.printEdge(0, 1)
        self.current.down.printEdge(1, 1)
        self.current.down.printEdge(2, 1)


    def turnCube(self):
        dir = int(input(
            "\n\t[1] Right\t\t[2] Left\n\t[3] Up\t\t\t[4] Down\n\t[0] See opposite face.\n\nEnter Direction::\t"))
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

    def showState(self):
        self.current.showFace()

    def getDirection(self):
        x = int(
            input("\n\t\t[1] Up\t\t[2] Down\n\t\t[3] Left\t[4] Right\n\nEnter Side::"))-1

        if x <= 3 and x >= 0:
            y = int(
                input("\n\t\t[1] Left\t\t[2] Right\n\nEnter Direction::\t"))-1
        else:
            print("Invalid Input\n")
            self.getDirection()

        self._rotate(self, x, y)

    def _rotate(self, side, direc):
        pass
