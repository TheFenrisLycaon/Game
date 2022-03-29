import os

# TODO : Configure Moves


def clear():
    """Clearing the screen"""
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def banner():
    """Printing banner"""
    print("  _____ _                    ")
    print(" / ____| |                   ")
    print("| |    | |__   ___  ___ ___  ")
    print("| |    | '_ \ / _ \/ __/ __| ")
    print("| |____| | | |  __/\__ \__ \\")
    print(" \_____|_| |_|\___||___/___/ ")
    print("                             ")
