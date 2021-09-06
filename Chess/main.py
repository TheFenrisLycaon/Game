from utils import clear, banner
from session import *

WHITE = 0
BLACK = 1 

if __name__ == "__main__":
    turn = WHITE
    while True:
        clear()
        banner()
        b = board()
        b.show(turn)
        input()
        turn = not turn
        
