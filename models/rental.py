from client import Client
from car import Car

class Rental:
    def __init__(self, client: Client, car: Car, rentDate, returnDate):
        self._client = client     
        self._car = car            
        self._rentDate = rentDate
        self._returnDate = returnDate
        self._car._isAvailable(False)

    def get_client(self):
        return self._client

    def get_car(self):
        return self._car

    def set_rent(self, rent: str):
        self._rentDate = rent

    def set_return(self, giveback: str):
        self._returnDate = giveback

    def get_rent(self):
        return self._rentDate
    
    def get_return(self):
        return self._returnDate
