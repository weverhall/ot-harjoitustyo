<<<<<<< HEAD
from ui.lookup_view import LookupView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_lookup_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def handle_lookup_view(self):
        self._show_lookup_view()

    def _show_lookup_view(self):
        self._hide_current_view()
        self._current_view = LookupView(
            self._root, 
            self.handle_lookup_view
        )
        self._current_view.grid()
=======
from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root
>>>>>>> 4aaace358a7d0c2ff4fec776779a4620c9ff7304
