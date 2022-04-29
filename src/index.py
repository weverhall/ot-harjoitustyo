from tkinter import Tk
from ui.ui import UI
from platform import system as platform_os


def main():
    window = Tk()

    if platform_os().lower() == "linux":
        window.config(background="gray85")
    window.title("NetLookApp")
    

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()
