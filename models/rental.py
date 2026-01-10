from models.client import Client
from models.car import Car

class Rental:
    def __init__(self, client: Client, car: Car, rent_date: str, return_date: str):
        self._client = client
        self._car = car
        self._rent_date = rent_date
        self._return_date = return_date

    def get_client(self) -> Client:
        return self._client

    def get_car(self) -> Car:
        return self._car

    def set_rent(self, rent_date: str) -> None:
        self._rent_date = rent_date

    def set_return(self, return_date: str) -> None:
        self._return_date = return_date

    def get_rent(self) -> str:
        return self._rent_date

    def get_return(self) -> str:
        return self._return_date
