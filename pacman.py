import os
import time

def clear():
    os.system('clear')

def move(x, y):
    print("\033[%d;%dH" % (x, y))

def draw_pacman(x, y):
    move(x, y)
    print("  \033[1;33;40m<  \033[1;37;40m>\033[0m")
    move(x+1, y)
    print(" \033[1;33;40m/    \\\033[0m")
    move(x+2, y)
    print("\033[1;33;40m/      \\\033[0m")

def draw_ghost(x, y):
    move(x, y)
    print("\033[1;31;40m███████\033[0m")
    move(x+1, y)
    print("\033[1;31;40m█\033[1;37;40m░░░░░░░\033[1;31;40m█\033[0m")
    move(x+2, y)
    print("\033[1;31;40m█\033[1;37;40m░░░░░░░\033[1;31;40m█\033[0m")
    move(x+3, y)
    print("\033[1;31;40m█\033[1;37;40m░░░░░░░\033[1;31;40m█\033[0m")
    move(x+4, y)
    print("\033[1;31;40m███████\033[0m")

def main():
    clear()
    draw_pacman(10, 10)
    draw_ghost(10, 30)
    time.sleep(5)

if __name__ == "__main__":
    main()