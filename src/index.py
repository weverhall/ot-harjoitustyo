from tkinter import Tk
from platform import system as platform_os
from ui.ui import UI


def main():
    window = Tk()

    window.resizable(False, False)

    if platform_os().lower() == "linux":
        window.config(background="gray85")
    window.title("NetLookApp")

    UI(window).start()

    window.mainloop()


if __name__ == '__main__':
    main()
