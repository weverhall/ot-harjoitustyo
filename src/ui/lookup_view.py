from tkinter import ttk
from services.lookup_service import NetworkLookup


class LookupView:
    """User interface class responsible for the lookup view

    Attributes:
        root: Parent element
        network_lookup: NetworkLookup class object
        handle_show_main_view: UI-class method that replaces current view with the main view
    """

    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._network_lookup = NetworkLookup()
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._initialize()

    def grid(self):
        """Grids UI-elements to frame"""

        self._frame.grid()

    def destroy(self):
        """Removes current view"""

        self._frame.destroy()

    def _handle_domain_button_click(self):
        """Fetch Data button's functionality"""

        entry_value = self.domain_name_entry.get()
        output_value = self._network_lookup.domain_lookup(entry_value)

        self._label_domain_button.config(text=output_value,
                                         font=("Arial", "10"))
        self._label_domain_button.grid(
            sticky="NW", row=4, column=0, padx=3, pady=3)

        if output_value[:19] == "Domain is available":
            self._label_domain_button.configure(foreground="green")
        elif output_value[:15] == "Domain is taken":
            self._label_domain_button.configure(foreground="blue")
        else:
            self._label_domain_button.configure(foreground="red")

    def _initialize(self):
        """Initializes current view"""

        self._frame = ttk.Frame(master=self._root)

        self.domain_name_entry = ttk.Entry(master=self._frame)
        self._label_domain_button = ttk.Label(master=self._frame)

        self._label_heading = ttk.Label(
            master=self._frame,
            text="Type in domain name or IP\n"
                 "(e.g. mooc.fi or 128.214.9.98)",
            font=("Arial", "14"))

        domain_check_button = ttk.Button(
            master=self._frame,
            text="Fetch Data",
            command=self._handle_domain_button_click)

        main_view_button = ttk.Button(
            master=self._frame,
            text="🢦",
            command=self._handle_show_main_view)

        main_view_button.grid(sticky="NW", row=0, column=0,
                              padx=3, pady=3)

        self._label_heading.grid(sticky="W", row=1, column=0,
                                 padx=3, pady=7)

        self.domain_name_entry.grid(sticky="NW", row=2, column=0,
                                    padx=3, pady=3, ipadx=20, ipady=2)

        domain_check_button.grid(sticky="NW", row=3, column=0,
                                 padx=3, pady=3, ipadx=7, ipady=2)
