import sqlite3
from database.database_manager import DatabaseManager
from models.client import Client

class ClientRepository:
    def __init__(self, db: DatabaseManager):
        self._db = db

    def add_client(self, client: Client) -> int:
        query = "INSERT INTO clients (name, surname, phone, email) VALUES (?, ?, ?, ?)"
        params = (client.get_name(), client.get_surname(), client.get_phone(), client.get_email())
        try:
            return self._db.execute(query, params)
        except sqlite3.IntegrityError:
            raise ValueError("Klient o tym numerze telefonu już istnieje.")

    def get_all_clients(self):
        return self._db.fetch_all("SELECT * FROM clients ORDER BY id DESC")

    def get_client(self, client_id: int):
        return self._db.fetch_one("SELECT * FROM clients WHERE id = ?", (int(client_id),))

    def get_client_by_phone(self, phone: str):
        return self._db.fetch_one("SELECT * FROM clients WHERE phone = ?", (phone,))

    def delete_client(self, client_id: int) -> None:
        self._db.execute("DELETE FROM clients WHERE id = ?", (int(client_id),))
