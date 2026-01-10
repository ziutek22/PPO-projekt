import sqlite3
from database.database_manager import DatabaseManager

class RentalRepository:
    def __init__(self, db: DatabaseManager):
        self._db = db

    def add_rental(self, car_id: int, client_id: int, start_date: str, end_date: str, total_price: float) -> int:
        query = """
            INSERT INTO rentals (car_id, client_id, start_date, end_date, total_price)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (int(car_id), int(client_id), start_date, end_date, float(total_price))
        return self._db.execute(query, params)

    def get_rental(self, rental_id: int):
        return self._db.fetch_one("SELECT * FROM rentals WHERE id = ?", (int(rental_id),))

    def get_all_rentals(self):
        query = """
            SELECT r.id,
                   r.start_date,
                   r.end_date,
                   r.total_price,
                   c.name || ' ' || c.surname AS client,
                   ca.brand || ' ' || ca.model || ' (' || ca.plate_number || ')' AS car
            FROM rentals r
            JOIN clients c ON c.id = r.client_id
            JOIN cars ca ON ca.id = r.car_id
            ORDER BY r.id DESC
        """
        return self._db.fetch_all(query, ())
