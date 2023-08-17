import figureMenu as fig

from rectangle import area as ra
from circle import area as ca
from square import area as sa
from triangle import area as ta

#main program

while(True):
    fig.figMenu()
    n = int(input("\tEnter your Choice: "))
    match(n):
        case 1:
            ra()
        case 2:
            ca()
        case 3:
            sa()
        case 4:
            ta()
        case 5:
            print("😍 Thanks for using the program 😍")
            break
        case _:
            print("🙄 Your Selection Choice is Wrong - Try again..! 🙄")