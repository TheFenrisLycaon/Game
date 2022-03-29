from pieces import *

EMPTY = " "


class board:
    def __init__(self):

        rwl = self.rwl = rook(1, 0, 0)
        nwl = self.nwl = knight(1, 0, 1)
        bwl = self.bwl = bishop(1, 0, 2)
        qw = self.qw = queen(1, 0, 3)
        kw = self.kw = king(1, 0, 4)
        rwr = self.rwr = rook(1, 0, 5)
        nwr = self.nwr = knight(1, 0, 6)
        bwr = self.bwr = bishop(1, 0, 7)
        pw_1 = self.pw_1 = pawn(1, 1, 0)
        pw_2 = self.pw_2 = pawn(1, 1, 1)
        pw_3 = self.pw_3 = pawn(1, 1, 2)
        pw_4 = self.pw_4 = pawn(1, 1, 3)
        pw_5 = self.pw_5 = pawn(1, 1, 4)
        pw_6 = self.pw_6 = pawn(1, 1, 5)
        pw_7 = self.pw_7 = pawn(1, 1, 6)
        pw_8 = self.pw_8 = pawn(1, 1, 7)
        pb_1 = self.pb_1 = pawn(0, 6, 0)
        pb_2 = self.pb_2 = pawn(0, 6, 1)
        pb_3 = self.pb_3 = pawn(0, 6, 2)
        pb_4 = self.pb_4 = pawn(0, 6, 3)
        pb_5 = self.pb_5 = pawn(0, 6, 4)
        pb_6 = self.pb_6 = pawn(0, 6, 5)
        pb_7 = self.pb_7 = pawn(0, 6, 6)
        pb_8 = self.pb_8 = pawn(0, 6, 7)
        rbl = self.rbl = rook(0, 7, 0)
        nbl = self.nbl = knight(0, 7, 1)
        bbl = self.bbl = bishop(0, 7, 2)
        qb = self.qb = queen(0, 7, 3)
        kb = self.kb = king(0, 7, 4)
        rbr = self.rbr = rook(0, 7, 5)
        nbr = self.nbr = knight(0, 7, 6)
        bbr = self.bbr = bishop(0, 7, 7)

        self.status = [
            [rwl, nwl, bwl, kw, qw, bwr, nwr, rwr],
            [pw_1, pw_2, pw_3, pw_4, pw_5, pw_6, pw_7, pw_8],
            *[[EMPTY] * 8 for _ in range(4)],
            [pb_1, pb_2, pb_3, pb_4, pb_5, pb_6, pb_7, pb_8],
            [rbl, nbl, bbl, qb, kb, bbr, nbr, rbr],
        ]

    def show(self, flipStatus=False):
        if flipStatus:
            for row in self.status:
                print(" --------------------------------------")
                print("|", end="")
                for p in row:
                    print(p, " | ", end="")
                print("")
            print(" --------------------------------------")
        else:
            for row in reversed(self.status):
                print(" --------------------------------------")
                print("|", end="")
                for p in reversed(row):
                    print(p, " | ", end="")
                print("")
            print(" --------------------------------------")
