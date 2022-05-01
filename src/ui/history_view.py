from tkinter import ttk
import tkinter
from services.lookup_service import NetworkLookup

from repositories.history_repository import(
    history_repository as default_history_repository)


class HistoryView:
    def __init__(self, root, handle_show_main_view,
                history_repository = default_history_repository):
        self._root = root
        self._frame = None
        self._history_repository = history_repository
        self._handle_show_main_view = handle_show_main_view
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _display_history_table(self):
        columns = ("Domain", "IP/FQDN", "Ping", "Date")
        tree = ttk.Treeview(master=self._frame, columns=columns, show="headings")
        tree.heading("Domain", text="Domain")
        tree.heading("IP/FQDN", text="IP/FQDN")
        tree.heading("Ping", text="Ping")
        tree.heading("Date", text="Date")

        rows = NetworkLookup.fetch_history(self)
        for row in rows:
            tree.insert("", tkinter.END, values=row)

        scrollbar = ttk.Scrollbar(master=self._frame,\
                                  orient=tkinter.VERTICAL,\
                                  command=tree.yview)
        
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky="ns")
        tree.grid(row=2, column=0, sticky="nsew")


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._display_history_table()

        main_view_button = ttk.Button(
            master=self._frame,
            text="🢦",
            command=self._handle_show_main_view)

        delete_history_button = ttk.Button(
            master=self._frame,
            text="Clear History",
            command=NetworkLookup.clear_history(self))

        main_view_button.grid(sticky="NW", row=0, column=0,
                            padx=3, pady=3)
        delete_history_button.grid(sticky="NW", row=4, column=0,
                                    padx=3, pady=3, ipadx=7, ipady=2)