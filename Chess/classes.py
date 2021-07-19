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


class ELEMENT:
    class WHITE:
        ROOK = "♜"
        KNIGHT = "♞"
        BISHOP = "♝"
        QUEEN = "♛"
        KING = "♚"
        PAWN = "♟"

    class BLACK:
        PAWN = "♙"
        ROOK = "♖"
        KNIGHT = "♘"
        BISHOP = "♗"
        QUEEN = "♕"
        KING = "♔"


class board:
    def __init__(self):
        rwl = rook(ELEMENT.WHITE.ROOK)
        nwl = knight(ELEMENT.WHITE.KNIGHT)
        bwl = bishop(ELEMENT.WHITE.BISHOP)
        qw = queen(ELEMENT.WHITE.QUEEN)
        kw = king(ELEMENT.WHITE.KING)
        rwr = rook(ELEMENT.WHITE.ROOK)
        nwr = knight(ELEMENT.WHITE.KNIGHT)
        bwr = bishop(ELEMENT.WHITE.BISHOP)
        pw = pawn(ELEMENT.WHITE.PAWN)
        rbl = rook(ELEMENT.BLACK.ROOK)
        nbl = knight(ELEMENT.BLACK.KNIGHT)
        bbl = bishop(ELEMENT.BLACK.BISHOP)
        qb = queen(ELEMENT.BLACK.QUEEN)
        kb = king(ELEMENT.BLACK.KING)
        rbr = rook(ELEMENT.BLACK.ROOK)
        nbr = knight(ELEMENT.BLACK.KNIGHT)
        bbr = bishop(ELEMENT.BLACK.BISHOP)
        pb = pawn(ELEMENT.BLACK.PAWN)

        self.status = [
            [
                rwl, nwl, bwl, kw, qw, bwr, nwr, rwr
            ],
            [pw for _ in range(8)],
            *[[" "] * 8 for _ in range(4)],
            [pb for _ in range(8)],
            [
                rbl,  nbl, bbl, qb, kb,  bbr, nbr, rbr
            ],
        ]

    def flip(self):
        return [row[::-1] for row in reversed(self.status)]

    def show(self, flipStatus=False):
        if flipStatus:
            for row in self.status:
                print(" --------------------------------------")
                print('|', end="")
                for p in row:
                    print(p, ' | ', end="")
                print("")
            print(" --------------------------------------")
        else:
            for row in reversed(self.status):
                print(" --------------------------------------")
                print('|', end="")
                for p in reversed(row):
                    print(p, ' | ', end="")
                print("")
            print(" --------------------------------------")


class Peice:
    def __int__(self):
        self.character = " "
        self.position = [0, 0]

    def __repr__(self) -> str:
        return self.character

    def __str__(self):
        return self.character


class pawn(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass


class bishop(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass


class knight(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass


class rook(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass


class queen(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass


class king(Peice):
    def __init__(self, c):
        self.character = c

    def positionUpdate(self, x, y):
        self.position = [x, y]

    def move(self):
        pass
