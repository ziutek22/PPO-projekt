import datetime
from models.car import Car


class CarManager:
    def __init__(self, repo):
        self._repo = repo

    def add_car(self, brand, model, year, plate_number, price_per_day):
        brand = (brand or "").strip()
        model = (model or "").strip()
        plate_number = (plate_number or "").strip().upper()
        year = (year or "").strip()
        price_per_day = (price_per_day or "").strip()

        if len(brand) < 2:
            return False, "Błąd: nieprawidłowa marka."
        if len(model) < 1:
            return False, "Błąd: nieprawidłowy model."
        if len(plate_number) < 3:
            return False, "Błąd: nieprawidłowy numer rejestracyjny."

        try:
            year_int = int(year)
        except:
            return False, "Błąd: rok musi być liczbą."

        current_year = datetime.datetime.now().year
        if year_int < 1950 or year_int > current_year + 1:
            return False, "Błąd: nieprawidłowy rok."

        try:
            price_float = float(price_per_day)
        except:
            return False, "Błąd: cena musi być liczbą."

        if price_float <= 0:
            return False, "Błąd: cena musi być większa od 0."

        fuel = "Benzyna"
        car = Car(brand, model, year_int, fuel, True, price_float, plate_number)

        try:
            new_id = self._repo.add_car(car)
            return True, f"Dodano samochód (ID={new_id})."
        except Exception as e:
            return False, str(e)

    def update_car(self, car_id, brand, model, year, plate_number, price_per_day):
        brand = (brand or "").strip()
        model = (model or "").strip()
        plate_number = (plate_number or "").strip().upper()
        year = (year or "").strip()
        price_per_day = (price_per_day or "").strip()

        if not str(car_id).isdigit():
            return False, "Błąd: nieprawidłowe ID."
        if len(brand) < 2 or len(model) < 1 or len(plate_number) < 3:
            return False, "Błąd: uzupełnij poprawnie dane."

        try:
            year_int = int(year)
            price_float = float(price_per_day)
        except:
            return False, "Błąd: rok/cena mają zły format."

        current_year = datetime.datetime.now().year
        if year_int < 1950 or year_int > current_year + 1:
            return False, "Błąd: nieprawidłowy rok."
        if price_float <= 0:
            return False, "Błąd: cena musi być większa od 0."

        try:
            self._repo.update_car(int(car_id), brand, model, year_int, plate_number, price_float)
            return True, "Zapisano zmiany."
        except Exception as e:
            return False, str(e)

    def set_available(self, car_id, status):
        try:
            self._repo.set_availability(int(car_id), bool(status))
            return True, "Zmieniono dostępność."
        except Exception as e:
            return False, str(e)

    def delete_car(self, car_id):
        try:
            self._repo.delete_car(int(car_id))
            return True, "Usunięto samochód."
        except Exception as e:
            return False, str(e)

    def get_all_cars(self):
        return self._repo.get_all_cars()
