class Vehicle:
    def __init__(self, brand, model, productionYear):
        self._brand = brand
        self._model = model
        self._productionYear = productionYear

    def set_brand(self, setBrand: str):
        self._brand = setBrand

    def set_model(self, setModel: str):
        self._model = setModel
    
    def set_year(self, year: float):
        self._productionYear = year

    def get_brand(self):
        return self._brand
    
    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._productionYear