import tkinter as tk
from tkinter import ttk, messagebox

class RentalsWindow(tk.Toplevel):
    def __init__(self, master, rental_manager, car_manager, client_manager):
        super().__init__(master)
        self.title("Wypożyczenia")
        self.geometry("980x460")
        self.resizable(False, False)

        self._rental_manager = rental_manager
        self._car_manager = car_manager
        self._client_manager = client_manager

        columns = ("id", "client", "car", "start", "end", "total")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)
        for c, w in zip(columns, (60, 240, 300, 120, 120, 120)):
            self.tree.heading(c, text=c)
            self.tree.column(c, width=w, anchor="center")
        self.tree.place(x=10, y=10)

        form = ttk.LabelFrame(self, text="Dodaj wypożyczenie")
        form.place(x=10, y=280, width=960, height=170)

        ttk.Label(form, text="Klient").grid(row=0, column=0, padx=6, pady=8, sticky="w")
        ttk.Label(form, text="Samochód (dostępne)").grid(row=0, column=2, padx=6, pady=8, sticky="w")
        ttk.Label(form, text="Start (YYYY-MM-DD)").grid(row=1, column=0, padx=6, pady=8, sticky="w")
        ttk.Label(form, text="Koniec (YYYY-MM-DD)").grid(row=1, column=2, padx=6, pady=8, sticky="w")

        self.client_cb = ttk.Combobox(form, width=35, state="readonly")
        self.car_cb = ttk.Combobox(form, width=40, state="readonly")
        self.start_entry = ttk.Entry(form, width=18)
        self.end_entry = ttk.Entry(form, width=18)

        self.client_cb.grid(row=0, column=1, padx=6, pady=8, sticky="w")
        self.car_cb.grid(row=0, column=3, padx=6, pady=8, sticky="w")
        self.start_entry.grid(row=1, column=1, padx=6, pady=8, sticky="w")
        self.end_entry.grid(row=1, column=3, padx=6, pady=8, sticky="w")

        ttk.Button(form, text="Utwórz wypożyczenie", command=self.add_rental).grid(row=2, column=0, padx=6, pady=10)
        ttk.Button(form, text="Odśwież listy", command=self.refresh_lists).grid(row=2, column=1, padx=6, pady=10)
        ttk.Button(form, text="Odśwież tabelę", command=self.refresh).grid(row=2, column=2, padx=6, pady=10)

        self._clients_map = {}
        self._cars_map = {}

        self.refresh_lists()
        self.refresh()

    def refresh_lists(self):
        # klienci
        clients = self._client_manager.get_all_clients()
        client_items = []
        self._clients_map.clear()
        for c in clients:
            label = f'{c["id"]}: {c["name"]} {c["surname"]} ({c["phone"]})'
            self._clients_map[label] = int(c["id"])
            client_items.append(label)
        self.client_cb["values"] = client_items
        if client_items:
            self.client_cb.current(0)

        # samochody dostępne
        cars = self._car_manager.get_all_cars()
        car_items = []
        self._cars_map.clear()
        for ca in cars:
            if int(ca["available"]) == 1:
                label = f'{ca["id"]}: {ca["brand"]} {ca["model"]} {ca["plate_number"]} | {ca["price_per_day"]} zł/dzień'
                self._cars_map[label] = int(ca["id"])
                car_items.append(label)
        self.car_cb["values"] = car_items
        if car_items:
            self.car_cb.current(0)

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in self._rental_manager.get_all_rentals():
            self.tree.insert("", "end", values=(
                row["id"], row["client"], row["car"], row["start_date"], row["end_date"], row["total_price"]
            ))

    def add_rental(self):
        if not self.client_cb.get() or not self.car_cb.get():
            messagebox.showwarning("Info", "Dodaj klienta i samochód (dostępny), żeby utworzyć wypożyczenie.")
            return

        client_id = self._clients_map[self.client_cb.get()]
        car_id = self._cars_map[self.car_cb.get()]

        ok, msg = self._rental_manager.create_rental(car_id, client_id, self.start_entry.get(), self.end_entry.get())
        if ok:
            messagebox.showinfo("OK", msg)
            self.refresh_lists()
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)
