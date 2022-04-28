from tkinter import ttk


class HistoryView:
    def __init__(self, root, handle_show_lookup_view):
        self._root = root
        self._frame = None
        self._handle_show_lookup_view = handle_show_lookup_view
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        return_button = ttk.Button(
            master=self._frame, 
            text="Return to network lookup",
            command=self._handle_show_lookup_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=150)  
        return_button.grid(row=0, column=0, padx=2, pady=2)