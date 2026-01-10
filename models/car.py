from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        production_year: int,
        fuel_type: str,
        is_available: bool,
        price_per_day: float,
        plates: str
    ):
        super().__init__(brand, model, production_year)
        self._fuel_type = fuel_type
        self._is_available = is_available
        self._price_per_day = price_per_day
        self._plates = plates

    def set_fuel(self, fuel: str) -> None:
        self._fuel_type = fuel

    def set_availability(self, status: bool) -> None:
        self._is_available = bool(status)

    def set_price(self, price_per_day: float) -> None:
        self._price_per_day = float(price_per_day)

    def set_plates(self, plates: str) -> None:
        self._plates = plates

    def get_fuel(self) -> str:
        return self._fuel_type

    def get_availability(self) -> bool:
        return self._is_available

    def get_price(self) -> float:
        return float(self._price_per_day)

    def get_plates(self) -> str:
        return self._plates
