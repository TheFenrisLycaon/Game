from classes import *

if __name__ == "__main__":
    utils.clear()
    utils.banner()
    b = board()
    print("\nWhite's Perspective\n")
    b.show()
    b.flip()
    print("\nBlack's Perspective\n")
    b.show(1)
