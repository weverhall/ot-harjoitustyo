from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()

    window.geometry("390x250")

    window.title('Network Lookup App')

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()