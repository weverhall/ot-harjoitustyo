from tkinter import Tk, ttk, constants
from services.lookup_service import NetworkLookup


class LookupView:
    def __init__(self, root, handle_lookup_view):
        self._root = root
        self._frame = None
        self._initialize()
        self._handle_lookup_view = handle_lookup_view
        self._label_domain_button = ttk.Label(master=self._root)
        self._label_ip_button = ttk.Label(master=self._root)
        self._label_mac_button = ttk.Label(master=self._root)

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()
    
    def _handle_domain_button_click(self):
        entry_value = self.domain_name_entry.get()
        output_value = NetworkLookup.domain_lookup(self, entry_value)

        self._label_domain_button.config(text=output_value)
        self._label_domain_button.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5)

        if output_value == "Domain is available!":
            self._label_domain_button.configure(foreground="green")
        elif output_value[0:23] == "Domain is already taken":
            self._label_domain_button.configure(foreground="red")
        else:
            self._label_domain_button.configure(foreground="")

    def _handle_ip_mac_button_click(self):
        output_ip = NetworkLookup.find_own_ip(self)
        self._label_ip_button.config(text=output_ip,
        foreground="blue")
        self._label_ip_button.grid(
            sticky="N", row=8, column=0, columnspan=2, padx=5, pady=5)

        output_mac = NetworkLookup.find_own_mac(self)
        self._label_mac_button.config(text=output_mac,
        foreground="blue")
        self._label_mac_button.grid(
            sticky="N", row=9, column=0, columnspan=2, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self.domain_name_entry = ttk.Entry(master=self._root)

        domain_check_button = ttk.Button(
            master=self._root, 
            text="Type in a domain name to check its availability (e.g. mooc.fi)",
            command=self._handle_domain_button_click)

        ip_mac_fetch_button = ttk.Button(
            master=self._root, 
            text="Fetch your IP & MAC",
            command=self._handle_ip_mac_button_click)
               
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)  
        self.domain_name_entry.grid(sticky="N", row=0, column=0, columnspan=2, padx=5, pady=5)    
        domain_check_button.grid(sticky="N", row=1, column=0, columnspan=2, padx=5, pady=5) 
        ip_mac_fetch_button.grid(sticky="N", row=7, column=0, columnspan=2, padx=5, pady=5)
        

        