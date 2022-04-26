from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()

    window.geometry("445x250")

    window.title("NetLookApp")

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()
