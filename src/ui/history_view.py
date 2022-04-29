from tkinter import ttk


class HistoryView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._frame = None
        self._handle_show_main_view = handle_show_main_view
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        main_view_button = ttk.Button(
            master=self._frame,
            text="Return to Main Menu",
            command=self._handle_show_main_view)

        main_view_button.pack(sticky="NW", row=0, column=0, rowspan=1, 
                            padx=3, pady=3, ipadx=15, ipady=3)