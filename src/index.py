from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()

    window.geometry("426x240")
    window.title("NetLookApp")
    window["bg"] = "SystemButtonFace"

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()
