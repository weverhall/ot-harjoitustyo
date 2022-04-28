from tkinter import ttk
from services.lookup_service import NetworkLookup


class LookupView:
    def __init__(self, root, handle_show_main_view):
        self._root = root
        self._frame = None
        self._handle_show_main_view = handle_show_main_view
        self._initialize()

    def grid(self):
        self._frame.grid()

    def destroy(self):
        self._frame.destroy()

    def _handle_domain_button_click(self):
        entry_value = self.domain_name_entry.get()
        output_value = NetworkLookup.domain_lookup(self, entry_value)

        self._label_domain_button.config(text=output_value,
            font=("Arial", "10"))
        self._label_domain_button.grid(
            sticky="W", row=3, column=0, padx=3, pady=3)

        if output_value[:19] == "Domain is available":
            self._label_domain_button.configure(foreground="green")
        elif output_value[:15] == "Domain is taken":
            self._label_domain_button.configure(foreground="blue")
        else:
            self._label_domain_button.configure(foreground="red")


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.domain_name_entry = ttk.Entry(master=self._frame)
        self._label_domain_button = ttk.Label(master=self._frame)

        self._label_heading = ttk.Label(
            master=self._frame,
            text="Type in domain name or IP to fetch domain data\n"
                 "(e.g. mooc.fi or 128.214.9.98)",
            font=("Arial", "14"),
            foreground="black")

        domain_check_button = ttk.Button(
            master=self._frame, 
            text="Enter",
            command=self._handle_domain_button_click)

        main_view_button = ttk.Button(
            master=self._frame,
            text="Return to Main Menu",
            command=self._handle_show_main_view)
               
        self._label_heading.grid(row=0, column=0, padx=5, pady=3)

        self.domain_name_entry.grid(sticky="NW", row=1, column=0, 
                                    padx=5, pady=5, ipadx=61, ipady=1)
        main_view_button.grid(sticky="NW", row=2, column=0, 
                                    padx=5, pady=5, ipadx=15, ipady=2) 
        domain_check_button.grid(row=2, column=0, 
                                    padx=5, pady=5, ipadx=7, ipady=2) 