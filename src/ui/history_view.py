from tkinter import ttk
import tkinter
from services.lookup_service import NetworkLookup
from repositories.history_repository import(
    history_repository as default_history_repository)


class HistoryView:
    """User interface class that's responsible for the history view

    Attributes:
        root: Parent element
        handle_show_main_view: UI-class method that replaces current view with the main view
        history_repository: HistoryRepository class object for treeview
    """

    def __init__(self, root, handle_show_main_view,
                 history_repository=default_history_repository):
        self._root = root
        self._network_lookup = NetworkLookup()
        self._handle_show_main_view = handle_show_main_view
        self._history_repository = history_repository
        self._frame = None
        self._initialize()

    def grid(self):
        """Grids UI-elements to frame"""

        self._frame.grid()

    def destroy(self):
        """Removes current view"""

        self._frame.destroy()

    def _display_history_table(self):
        """Renders treeview widget to frame"""      

        columns = ("Domain", "IP/FQDN", "Ping", "Date")
        tree = ttk.Treeview(master=self._frame,
                            columns=columns, 
                            show="headings")
        tree.heading("Domain", text="Domain")
        tree.heading("IP/FQDN", text="IP/FQDN")
        tree.heading("Ping", text="Ping")
        tree.heading("Date", text="Date")
        tree.column("Domain", minwidth=85, width=275)
        tree.column("IP/FQDN", minwidth=85, width=275)
        tree.column("Ping", minwidth=85, width=85)
        tree.column("Date", minwidth=85, width=85)


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

        tree.configure(yscroll=scrollbar.set, height=15)
        tree.tag_configure("even_row", background="white")
        tree.tag_configure("odd_row", background="aliceblue")
        
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        scrollbar.grid(row=2, column=1, sticky="NS")
        tree.grid(row=2, column=0, sticky="NSEW")

    def _initialize(self):
        """Initializes current view"""

        self._frame = ttk.Frame(master=self._root)

        self._display_history_table()

        main_view_button = ttk.Button(
            master=self._frame,
            text="🢦",
            command=self._handle_show_main_view)

        delete_history_button = ttk.Button(
            master=self._frame,
            text="Clear History",
            command=self._network_lookup.clear_history)

        main_view_button.grid(sticky="NW", row=0, column=0,
                              padx=3, pady=3)

        delete_history_button.grid(sticky="NW", row=4, column=0,
                                   padx=3, pady=3, ipadx=7, ipady=2)
