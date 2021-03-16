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
        self.center = self.red

    def showCube(self):
        self.red.showFace()
        self.blue.showFace()
        self.green.showFace()
        self.orange.showFace()
        self.yellow.showFace()
        self.white.showFace()

    def showState(self):
        self.center.showFace()
