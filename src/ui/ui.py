from ui.main_view import MainView
from ui.lookup_view import LookupView
from ui.history_view import HistoryView


class UI:
    """User interface class that's responsible for managing windows

    Attributes:
        root: Parent element
    """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        """Shows the main view when program is started"""

        self._show_main_view()

    def _hide_current_view(self):
        """Removes current view"""

        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_main_view(self):
        """Removes current view and shows the main view"""

        self._hide_current_view()
        self._current_view = MainView(
            self._root,
            self._show_lookup_view,
            self._show_history_view)
        self._current_view.grid()

    def _show_lookup_view(self):
        """Removes current view and shows the lookup view"""

        self._hide_current_view()
        self._current_view = LookupView(
            self._root,
            self._show_main_view)
        self._current_view.grid()

    def _show_history_view(self):
        """Removes current view and shows the history view"""

        self._hide_current_view()
        self._current_view = HistoryView(
            self._root,
            self._show_main_view)
        self._current_view.grid()
