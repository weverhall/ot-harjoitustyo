from tkinter import ttk
from services.lookup_service import NetworkLookup


class MainView:
    def __init__(self, root, handle_show_lookup_view, handle_show_history_view):
        self._root = root
        self._frame = None
        self._handle_show_lookup_view = handle_show_lookup_view
        self._handle_show_history_view = handle_show_history_view
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._label_heading = ttk.Label(
            master=self._frame,
            text="Welcome to NetLookApp:\nA Comfy Network Lookup Tool",
            font=("Arial", "14"),
            foreground="black")

        self._label_own_public_ip = ttk.Label(
            master=self._frame,
            text=NetworkLookup.find_own_public_ip(self),
            font=("Arial", "10"),
            foreground="blue")

        self._label_local_ip = ttk.Label(
            master=self._frame,
            text=NetworkLookup.find_local_ip(self),
            font=("Arial", "10"),
            foreground="blue")

        self._label_mac = ttk.Label(
            master=self._frame,
            text=NetworkLookup.find_mac(self),
            font=("Arial", "10"),
            foreground="blue")

        self.lookup_view_button = ttk.Button(
            master=self._frame,
            text="Domain Lookup",
            command=self._handle_show_lookup_view)

        self.history_view_button = ttk.Button(
            master=self._frame,
            text="Domain History",
            command=self._handle_show_history_view)

        self._frame.columnconfigure(0, minsize=275)
        self._label_heading.grid(sticky="NW", row=0, column=0, padx=5, pady=3)

        self.lookup_view_button.grid(sticky="NW", row=1, column=0,
                                     padx=5, pady=10, ipadx=7, ipady=2)
        self.history_view_button.grid(sticky="NE", row=1, column=0,
                                      padx=5, pady=10, ipadx=7, ipady=2)

        self._label_own_public_ip.grid(sticky="W", row=4, column=0, padx=5, pady=1)
        self._label_local_ip.grid(sticky="W", row=5, column=0, padx=5, pady=1)
        self._label_mac.grid(sticky="W", row=6, column=0, padx=5, pady=1)
