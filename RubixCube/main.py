#!/home/fenris/anaconda3/bin/python
from termcolor import cprint
from pyfiglet import figlet_format
import os
import sys
from colorama import init
from . import RubixCube
init(strip=not sys.stdout.isatty())


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


if __name__ == '__main___':
    clear()
    cprint(figlet_format('Rubixx Cube', font='big'), 'white', attrs=['bold'])
    x = RubixCube.rubixx()
    x.showState()
