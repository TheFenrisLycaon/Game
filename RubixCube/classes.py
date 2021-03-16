from itertools import cycle
import os
import sys


class Utils:
    def __init__(self):
        pass

    def clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def banner():
        print("  _ \        |    _)                 __|        |          ")
        print("    /  |  |   _ \  | \ \ / \ \ /    (     |  |   _ \   -_) ")
        print(" _|_\ \_,_| _.__/ _|  _\_\  _\_\   \___| \_,_| _.__/ \___| ")
        print()



class face:

    def __init__(self, color):
        self.color = color
        k = color[0].upper()
        self.right = face
        self.up = face
        self.down = face
        self.state = [[k, k, k]]*3

    def showFace(self):
        for i in range(3):
            print(self.state[i])


class rubixx:

    def __init__(self):
        self.red = face('red')
        self.blue = face('blue')
        self.green = face('green')
        self.white = face('white')
        self.orange = face('orange')
        self.yellow = face('yellow')
        self.red.right = self.blue
        self.blue.right = self.orange
        self.orange.right = self.green
        self.red.up = self.white
        self.blue.up = self.white
        self.orange.up = self.white
        self.red.down = self.yellow
        self.blue.down = self.yellow
        self.orange.down = self.yellow
        self.current = self.red

    def showCube(self):
        self.red.showFace()
        self.blue.showFace()
        self.green.showFace()
        self.orange.showFace()
        self.yellow.showFace()
        self.white.showFace()

    def showState(self):
        self.current.showFace()

    def getDirection(self):
        x = int(input("\n\t\t[1] Up\t\t[2] Down\n\t\t[3] Left\t[4] Right\n\nEnter Side::"))-1
        
        if x<=3 and x>=0:
            y = int(input("\n\t\t[1] Left\t\t[2] Right\n\nEnter Direction::\t"))-1
        else:
            print("Invalid Input\n")
            self.getDirection()

        self._rotate(self,x,y)

    def _rotate(self,side,direc):
        pass
