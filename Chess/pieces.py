EMPTY = " "


class Peice:
    def __int__(self):
        """ Initaializes a piece """
        self.WHITE = " "
        self.BLACK = " "
        self.character = " "
        self.position = [0, 0]

    def __repr__(self) -> str:
        """ Representation of the Character"""
        return self.character

    def __str__(self):
        """ Representation of the Character"""
        return self.character


class rook(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♜"
        self.BLACK = "♖"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.x = x
        self.y = y

    def move(self, board, direction, steps):
        """
        Direction : 0 is horizontal movement ; 1 is vertical movement
        Steps : Number of steps the piece moves
        """
        board[self.x][self.y] = EMPTY  # Clear current Position
        if direction == 1:
            self.x += steps
        else:
            self.y += steps
        board[self.y][self.x] = self.character
        return board


class knight(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♞"
        self.BLACK = "♘"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.position = [x, y]

    def move(self):
        pass


class bishop(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♝"
        self.BLACK = "♗"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.position = [x, y]

    def move(self):
        pass


class queen(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♛"
        self.BLACK = "♕"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.position = [x, y]

    def move(self):
        pass


class king(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♚"
        self.BLACK = "♔"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.position = [x, y]

    def move(self, newX, newY):
        if [newX, newY] != EMPTY:
            self.positionUpdate(newX, newY)


class pawn(Peice):
    def __init__(self, c, y, x):
        self.WHITE = "♟"
        self.BLACK = "♙"
        self.character = self.WHITE*c + self.BLACK*(not c)
        self.x, self.y = x, y
        self.c = c

    def move(self, board, killIntent=False, direction=-1, doubleStep=True):
        """
        killIntent : False is move ; True is kill
        direction : -1 for left ; 1 for right ; Needed when killIntent is True
        doubleStep :False for 1 step ; True for 2 ; Needed when at base
        """

        board[self.y][self.x] = EMPTY  # Clear current Position
        
        if killIntent:
            if self.c == 1:
                self.x += direction
                self.y += 1
            else:
                self.x += direction
                self.y -= 1
        else:
            if self.y == 1 or self.y == 6:
                if self.c == 1:
                    self.y = self.y + 1 + doubleStep
                else:
                    self.y = self.y - 1 - doubleStep
            else:
                if self.c == 1:
                    self.y += 1
                else:
                    self.y -= 1

        board[self.y][self.x] = self.character
        return board
