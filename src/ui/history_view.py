from tkinter import ttk


class HistoryView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._frame = None
        self._handle_show_main_view = handle_show_main_view
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        main_view_button = ttk.Button(
            master=self._frame,
            text="Return to Main Menu",
            command=self._handle_show_main_view)

        main_view_button.grid(sticky="NW", row=0, column=0)