import tkinter as tk
from tkinter import ttk, messagebox

class ClientsWindow(tk.Toplevel):
    def __init__(self, master, client_manager):
        super().__init__(master)
        self.title("Klienci")
        self.geometry("860x420")
        self.resizable(False, False)

        self._client_manager = client_manager

        columns = ("id", "name", "surname", "phone", "email")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)
        for c, w in zip(columns, (60, 160, 160, 160, 260)):
            self.tree.heading(c, text=c)
            self.tree.column(c, width=w, anchor="center")
        self.tree.place(x=10, y=10)

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        form = ttk.LabelFrame(self, text="Dodaj")
        form.place(x=10, y=270, width=840, height=140)

        self.var_name = tk.StringVar()
        self.var_surname = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_email = tk.StringVar()

        ttk.Label(form, text="Imię").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_name, width=18).grid(row=0, column=1, padx=6, pady=6)

        ttk.Label(form, text="Nazwisko").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_surname, width=18).grid(row=0, column=3, padx=6, pady=6)

        ttk.Label(form, text="Telefon").grid(row=0, column=4, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_phone, width=18).grid(row=0, column=5, padx=6, pady=6)

        ttk.Label(form, text="Email").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(form, textvariable=self.var_email, width=32).grid(row=1, column=1, padx=6, pady=6, columnspan=3, sticky="w")

        ttk.Button(form, text="Dodaj", command=self.add).grid(row=0, column=6, padx=10, pady=6)
        ttk.Button(form, text="Usuń", command=self.delete).grid(row=1, column=6, padx=10, pady=6)
        ttk.Button(form, text="Odśwież", command=self.refresh).grid(row=0, column=7, padx=10, pady=6)

        self.selected_id = None
        self.refresh()

    def _on_select(self, _):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.selected_id = int(values[0])

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in self._client_manager.get_all_clients():
            self.tree.insert("", "end", values=(row["id"], row["name"], row["surname"], row["phone"], row["email"] or ""))

    def add(self):
        ok, msg = self._client_manager.add_client(
            self.var_name.get(),
            self.var_surname.get(),
            self.var_phone.get(),
            self.var_email.get(),
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
        if not messagebox.askyesno("Potwierdzenie", "Usunąć wybranego klienta?"):
            return

        ok, msg = self._client_manager.delete_client(self.selected_id)
        if ok:
            self.selected_id = None
            messagebox.showinfo("OK", msg)
            self.refresh()
        else:
            messagebox.showerror("Błąd", msg)
