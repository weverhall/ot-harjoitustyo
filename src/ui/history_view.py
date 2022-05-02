from tkinter import ttk
import tkinter
from services.lookup_service import NetworkLookup
from repositories.history_repository import(
    history_repository as default_history_repository)


class HistoryView:
    def __init__(self, root, handle_show_main_view,
                 history_repository=default_history_repository):
        self._root = root
        self.network_lookup = NetworkLookup()
        self._history_repository = history_repository
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _display_history_table(self):
        columns = ("Domain", "IP/FQDN", "Ping", "Date")
        tree = ttk.Treeview(master=self._frame,
                            columns=columns, 
                            show="headings")
        tree.heading("Domain", text="Domain")
        tree.heading("IP/FQDN", text="IP/FQDN")
        tree.heading("Ping", text="Ping")
        tree.heading("Date", text="Date")
        tree.column("Domain", minwidth=80, width=250)
        tree.column("IP/FQDN", minwidth=80, width=250)
        tree.column("Ping", minwidth=80, width=80)
        tree.column("Date", minwidth=80, width=80)


        rows = NetworkLookup.fetch_history(self)
        count = 0
        for row in rows:
            if count % 2 == 0:
                tree.insert("", tkinter.END, 
                values=(row[0], row[1], row[2], row[3]),
                tags="even_row")
            else:
                tree.insert("", tkinter.END, 
                values=(row[0], row[1], row[2], row[3]),
                tags="odd_row")
            count += 1

        scrollbar = ttk.Scrollbar(master=self._frame,
                                  orient=tkinter.VERTICAL,
                                  command=tree.yview)

        tree.configure(yscroll=scrollbar.set, selectmode="browse")
        tree.tag_configure("odd_row", background="white")
        tree.tag_configure("even_row", background="aliceblue")
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        scrollbar.grid(row=2, column=1, sticky="NS")
        tree.grid(row=2, column=0, sticky="NSEW")

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
            command=self.network_lookup.clear_history)

        main_view_button.grid(sticky="NW", row=0, column=0,
                              padx=3, pady=3)

        delete_history_button.grid(sticky="NW", row=4, column=0,
                                   padx=3, pady=3, ipadx=7, ipady=2)

        
