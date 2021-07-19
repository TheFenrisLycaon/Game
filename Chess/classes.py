import os
import enum

# TODO : Set unicode for the Peices
# TODO : Configure Moves


class utils:
    def clear():
        """ Clearing the screen """
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def banner():
        """ Printing banner """
        print("  _____ _                    ")
        print(" / ____| |                   ")
        print("| |    | |__   ___  ___ ___  ")
        print("| |    | '_ \ / _ \/ __/ __| ")
        print("| |____| | | |  __/\__ \__ \\")
        print(" \_____|_| |_|\___||___/___/ ")
        print("                             ")


class Color:
    WHITE = 0
    BLACK = 1


class Position:
    pass


class board:
    def __init__(self):
        rwl = rook(0)
        pw = pawn(0)
        nwl = knight(0)
        bwl = bishop(0)
        kw = king(0)
        qw = queen(0)
        rbl = rook(1)
        pb = pawn(1)
        nbl = knight(1)
        bbl = bishop(1)
        kb = king(1)
        qb = queen(1)
        rwr = rook(0)
        nwr = knight(0)
        bwr = bishop(0)
        rbr = rook(1)
        pb = pawn(1)
        nbr = knight(1)
        bbr = bishop(1)
        kb = king(1)
        qb = queen(1)
        self.status = [
            [
                rwl, nwl, bwl, kw, qw, bwr, nwr, rwr
            ],
            [pw for _ in range(8)],
            *[[None] * 8 for _ in range(4)],
            [pb for _ in range(8)],
            [
                rbl,  nbl, bbl, qb, kb,  bbr, nbr, rbr
            ],
        ]

    def flip(self):
        return [row[::-1] for row in reversed(self.status)]

    def show(self, flipStatus=False):
        # for i, row in enumerate(self.status if not flipStatus else self.flip(self.status)):
        #     row_strings = [
        #         chrs.get(tile, chrs[(Color((i + j) % 2), Peice.EMPTY)])
        #         for j, tile in enumerate(row)
        #     ]
        #     print("".join(row_strings))
        print(self.status)


class Peice:
    def __int__(self):
        self.color = 0
        self.position = [0,0]


class pawn(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265F"
        # self.black = "\u2659"

    def move(self):
        pass


class bishop(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265D"
        # self.black = "\u2657"

    def move(self):
        pass


class knight(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265E"
        # self.black = "\u2654"

    def move(self):
        pass


class rook(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265C"
        # self.black = "\u2656"

    def move(self):
        pass


class queen(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265B"
        # self.black = "\u2655"

    def move(self):
        pass


class king(Peice):
    def __init__(self, c):
        super().color = Color.BLACK*c + Color.WHITE*c
    
    def positionUpdate(self,x,y):
        super().position = [x,y]
        # self.white = "\u265A"
        # self.black = "\u2654"

    def move(self):
        pass
