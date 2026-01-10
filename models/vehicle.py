class Vehicle:
    def __init__(self, brand: str, model: str, production_year: int):
        self._brand = brand
        self._model = model
        self._production_year = production_year

    def set_brand(self, brand: str) -> None:
        self._brand = brand

    def set_model(self, model: str) -> None:
        self._model = model

    def set_year(self, year: int) -> None:
        self._production_year = year

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._production_year
