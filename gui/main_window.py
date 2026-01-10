import tkinter as tk
from tkinter import ttk, messagebox

from gui.cars_window import CarsWindow
from gui.clients_window import ClientsWindow
from gui.rentals_window import RentalsWindow

class MainWindow(tk.Tk):
    def __init__(self, managers: dict):
        super().__init__()
        self.title("Wypożyczalnia samochodów - PPO")
        self.geometry("520x260")
        self.resizable(False, False)

        self._managers = managers

        title = tk.Label(self, text="System wypożyczalni samochodów", font=("Segoe UI", 14, "bold"))
        title.pack(pady=20)

        frame = ttk.Frame(self)
        frame.pack(pady=10)

        ttk.Button(frame, text="Samochody", width=20, command=self.open_cars).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(frame, text="Klienci", width=20, command=self.open_clients).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(frame, text="Wypożyczenia", width=20, command=self.open_rentals).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(self, text="Baza danych: SQLite (database/rental.db)").pack(pady=10)

    def open_cars(self):
        CarsWindow(self, self._managers["car_manager"])

    def open_clients(self):
        ClientsWindow(self, self._managers["client_manager"])

    def open_rentals(self):
        RentalsWindow(
            self,
            self._managers["rental_manager"],
            self._managers["car_manager"],
            self._managers["client_manager"],
        )
