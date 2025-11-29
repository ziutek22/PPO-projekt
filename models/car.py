from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, productionYear, fuelType, isAvailable, price, plates):
        super().__init__(brand, model, productionYear)
        self._fuelType = fuelType
        self._isAvailable = isAvailable
        self._price = price
        self._plates = plates

    def set_fuel(self, fuel: str):
        self._fuelType = fuel

    def set_availability(self, status: bool):
        self._isAvailable = status
    
    def set_price(self, money: float):
        self._price = money

    def set_plates(self, plateNumber: str):
        self._plates = plateNumber

    def get_fuel(self):
        return self._fuelType
    
    def get_availability(self):
        return self._isAvailable
    
    def get_price(self):
        return self._price
    
    def get_plates(self):
        return self._plates

    def get_info(self):
        return (
            f"Twój samochód to {self._brand} {self._model} o numerach rejestracyjnych {self._plates}\n"
            f"Utworzony w {self._productionYear}\n"
            f"Koszt wynajmu to {self._price} a dostępność {self._isAvailable}\n"
        )