import re
from models.client import Client


class ClientManager:
    def __init__(self, repo):
        self._repo = repo

    def add_client(self, name, surname, phone, email):
        name = (name or "").strip()
        surname = (surname or "").strip()
        phone = (phone or "").strip()
        email = (email or "").strip()

        if len(name) < 2:
            return False, "Błąd: nieprawidłowe imię."
        if len(surname) < 2:
            return False, "Błąd: nieprawidłowe nazwisko."
        if len(phone) < 6:
            return False, "Błąd: nieprawidłowy telefon."

        if email != "" and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            return False, "Błąd: nieprawidłowy email."

        client = Client(name, surname, phone, email)

        try:
            new_id = self._repo.add_client(client)
            return True, f"Dodano klienta (ID={new_id})."
        except Exception as e:
            return False, str(e)

    def delete_client(self, client_id):
        try:
            self._repo.delete_client(int(client_id))
            return True, "Usunięto klienta."
        except Exception as e:
            return False, str(e)

    def get_all_clients(self):
        return self._repo.get_all_clients()
