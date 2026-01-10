import sqlite3
from pathlib import Path
from typing import Any, Sequence, Optional

class DatabaseManager:

    def __init__(self, db_path: str = "database/rental.db"):
        self._db_path = db_path
        self._connection: Optional[sqlite3.Connection] = None
        self._cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> None:
        Path(self._db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection = sqlite3.connect(self._db_path)
        self._connection.row_factory = sqlite3.Row
        self._cursor = self._connection.cursor()

    def close(self) -> None:
        if self._connection:
            self._connection.close()
        self._connection = None
        self._cursor = None

    def create_tables(self) -> None:
        if not self._cursor:
            raise RuntimeError("Najpierw wywołaj connect()")

        # Klienci
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT
            );
            """
        )

        # Samochody
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                plate_number TEXT NOT NULL UNIQUE,
                price_per_day REAL NOT NULL,
                available INTEGER NOT NULL CHECK (available IN (0,1))
            );
            """
        )

        # Wypożyczenia
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS rentals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_id INTEGER NOT NULL,
                client_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                total_price REAL NOT NULL,
                FOREIGN KEY(car_id) REFERENCES cars(id),
                FOREIGN KEY(client_id) REFERENCES clients(id)
            );
            """
        )

        self._connection.commit()

    def execute(self, query: str, params: Sequence[Any] = ()) -> int:
        if not self._cursor:
            raise RuntimeError("Najpierw wywołaj connect()")
        self._cursor.execute(query, params)
        self._connection.commit()
        return self._cursor.lastrowid if self._cursor.lastrowid else 0

    def fetch_all(self, query: str, params: Sequence[Any] = ()) -> list[sqlite3.Row]:
        if not self._cursor:
            raise RuntimeError("Najpierw wywołaj connect()")
        self._cursor.execute(query, params)
        return self._cursor.fetchall()

    def fetch_one(self, query: str, params: Sequence[Any] = ()) -> Optional[sqlite3.Row]:
        if not self._cursor:
            raise RuntimeError("Najpierw wywołaj connect()")
        self._cursor.execute(query, params)
        return self._cursor.fetchone()
