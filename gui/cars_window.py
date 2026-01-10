import tkinter as tk
from tkinter import ttk, messagebox


class CarsWindow(tk.Toplevel):
    def __init__(self, master, car_manager):
        super().__init__(master)
        self.title("Samochody")
        self.geometry("900x450")
        self.resizable(False, False)

        self._car_manager = car_manager
        self.selected_id = None

        columns = ("id", "brand", "model", "year", "plate", "price", "available")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)
        widths = (60, 140, 140, 80, 140, 100, 90)
        for c, w in zip(columns, widths):
            self.tree.heading(c, text=c)
            self.tree.column(c, width=w, anchor="center")
        self.tree.place(x=10, y=10)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        form = ttk.LabelFrame(self, text="Dodaj / Edytuj")
        form.place(x=10, y=270, width=880, height=165)

        self.var_brand = tk.StringVar()
        self.var_model = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_plate = tk.StringVar()
        self.var_price = tk.StringVar()

        ttk.Label(form, text="Marka").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_brand, width=18).grid(row=0, column=1, padx=6, pady=6)

        ttk.Label(form, text="Model").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_model, width=18).grid(row=0, column=3, padx=6, pady=6)

        ttk.Label(form, text="Rok").grid(row=0, column=4, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_year, width=10).grid(row=0, column=5, padx=6, pady=6)

        ttk.Label(form, text="Rejestracja").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_plate, width=18).grid(row=1, column=1, padx=6, pady=6)

        ttk.Label(form, text="Cena / dzień").grid(row=1, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_price, width=18).grid(row=1, column=3, padx=6, pady=6)

        ttk.Button(form, text="Dodaj", command=self.add).grid(row=0, column=6, padx=10, pady=6)
        ttk.Button(form, text="Zapisz zmiany", command=self.update).grid(row=1, column=6, padx=10, pady=6)
        ttk.Button(form, text="Usuń", command=self.delete).grid(row=0, column=7, padx=10, pady=6)
        ttk.Button(form, text="Odśwież", command=self.refresh).grid(row=1, column=7, padx=10, pady=6)

        ttk.Button(form, text="Ustaw: dostępny", command=lambda: self.set_available(True)).grid(row=0, column=8, padx=10, pady=6)
        ttk.Button(form, text="Ustaw: niedostępny", command=lambda: self.set_available(False)).grid(row=1, column=8, padx=10, pady=6)

        self.refresh()

    def _on_select(self, _):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.selected_id = int(values[0])

        self.var_brand.set(values[1])
        self.var_model.set(values[2])
        self.var_year.set(values[3])
        self.var_plate.set(values[4])
        self.var_price.set(values[5])

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for row in self._car_manager.get_all_cars():
            available_txt = "TAK" if int(row["available"]) == 1 else "NIE"
            fuel = row["fuel"] if "fuel" in row.keys() else ""
            self.tree.insert("", "end", values=(
                row["id"], row["brand"], row["model"], row["year"],
                row["plate_number"], row["price_per_day"], available_txt
            ))

    def add(self):
        ok, msg = self._car_manager.add_car(
            self.var_brand.get(),
            self.var_model.get(),
            self.var_year.get(),
            self.var_plate.get(),
            self.var_price.get(),
        )
        if ok:
            messagebox.showinfo("OK", msg)
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)

    def update(self):
        if not self.selected_id:
            messagebox.showwarning("Info", "Najpierw wybierz rekord z listy.")
            return

        ok, msg = self._car_manager.update_car(
            self.selected_id,
            self.var_brand.get(),
            self.var_model.get(),
            self.var_year.get(),
            self.var_plate.get(),
            self.var_price.get(),
        )
        if ok:
            messagebox.showinfo("OK", msg)
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)

    def delete(self):
        if not self.selected_id:
            messagebox.showwarning("Info", "Najpierw wybierz rekord z listy.")
            return
        if not messagebox.askyesno("Potwierdzenie", "Usunąć wybrany samochód?"):
            return

        ok, msg = self._car_manager.delete_car(self.selected_id)
        if ok:
            self.selected_id = None
            messagebox.showinfo("OK", msg)
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)

    def set_available(self, status):
        if not self.selected_id:
            messagebox.showwarning("Info", "Najpierw wybierz rekord z listy.")
            return

        ok, msg = self._car_manager.set_available(self.selected_id, status)
        if ok:
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)
