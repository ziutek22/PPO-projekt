import datetime


class RentalManager:
    def __init__(self, rental_repo, car_repo, client_repo):
        self._rental_repo = rental_repo
        self._car_repo = car_repo
        self._client_repo = client_repo

    def _parse_date(self, value):
        try:
            return datetime.datetime.strptime(value.strip(), "%Y-%m-%d").date()
        except:
            return None

    def create_rental(self, car_id, client_id, start_date, end_date):
        # sprawdzenie istnienia auta
        car = self._car_repo.get_car(int(car_id))
        if not car:
            return False, "Błąd: nie znaleziono samochodu."

        if int(car["available"]) != 1:
            return False, "Błąd: samochód jest niedostępny."

        # sprawdzenie istnienia klienta
        client = self._client_repo.get_client(int(client_id))
        if not client:
            return False, "Błąd: nie znaleziono klienta."

        start = self._parse_date(start_date)
        end = self._parse_date(end_date)

        if not start or not end:
            return False, "Błąd: data musi być w formacie YYYY-MM-DD (np. 2026-01-10)."

        today = datetime.date.today()
        if start < today:
            return False, "Błąd: nie można dodać wypożyczenia w przeszłości."
        if end < today:
            return False, "Błąd: nie można ustawić zwrotu w przeszłości."
        if end < start:
            return False, "Błąd: data zwrotu nie może być wcześniejsza niż data wypożyczenia."

        days = (end - start).days + 1
        total = float(car["price_per_day"]) * days

        try:
            rental_id = self._rental_repo.add_rental(int(car_id), int(client_id), start.isoformat(), end.isoformat(), total)
            self._car_repo.set_availability(int(car_id), False)
            return True, f"Dodano wypożyczenie (ID={rental_id}, cena={total:.2f} zł)."
        except Exception as e:
            return False, str(e)

    def get_all_rentals(self):
        return self._rental_repo.get_all_rentals()
