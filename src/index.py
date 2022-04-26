from tkinter import Tk, ttk
from ui.ui import UI
from PIL import Image, ImageTk
from pathlib import Path

def main():
    window = Tk()

    window.geometry("445x250")

    icon_path = Path("icon.png")
    icon = ImageTk.PhotoImage(Image.open(icon_path))
    icon_label = ttk.Label(image=icon)
    icon_label.grid(row=0, column=3, columnspan=4, padx=2, pady=2) 

    window.title("NetLookApp")

    UI(window).start()

    window.mainloop()

if __name__ == '__main__':
    main()
