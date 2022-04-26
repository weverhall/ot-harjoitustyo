from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()

    window.geometry("455x255")

    window.title("NetLookApp")

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()
