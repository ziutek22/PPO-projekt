import sqlite3
from database.database_manager import DatabaseManager
from models.car import Car

class CarRepository:
    def __init__(self, db: DatabaseManager):
        self._db = db

    def add_car(self, car: Car) -> int:
        query = """
            INSERT INTO cars (brand, model, year, plate_number, price_per_day, available)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            car.get_brand(),
            car.get_model(),
            int(car.get_year()),
            car.get_plates(),
            float(car.get_price()),
            1 if car.get_availability() else 0
        )
        try:
            return self._db.execute(query, params)
        except sqlite3.IntegrityError:
            raise ValueError("Samochód o podanych numerach rejestracyjnych już istnieje.")

    def get_car(self, car_id: int):
        return self._db.fetch_one("SELECT * FROM cars WHERE id = ?", (car_id,))

    def get_car_by_plate(self, plate_number: str):
        return self._db.fetch_one("SELECT * FROM cars WHERE plate_number = ?", (plate_number,))

    def get_all_cars(self):
        return self._db.fetch_all("SELECT * FROM cars ORDER BY id DESC")

    def update_car(self, car_id: int, brand: str, model: str, year: int, plate_number: str, price_per_day: float):
        query = """
            UPDATE cars
            SET brand = ?, model = ?, year = ?, plate_number = ?, price_per_day = ?
            WHERE id = ?
        """
        params = (brand, model, int(year), plate_number, float(price_per_day), int(car_id))
        try:
            self._db.execute(query, params)
        except sqlite3.IntegrityError:
            raise ValueError("Nie można zapisać zmian - możliwy konflikt numeru rejestracyjnego.")

    def set_availability(self, car_id: int, available: bool) -> None:
        self._db.execute("UPDATE cars SET available = ? WHERE id = ?", (1 if available else 0, int(car_id)))

    def delete_car(self, car_id: int) -> None:
        self._db.execute("DELETE FROM cars WHERE id = ?", (int(car_id),))
