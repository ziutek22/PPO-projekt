class Client:
    def __init__(self, name, surname, phone, email):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._email = email


    def set_name(self, data: str):
        self._name = data

    def set_surname(self, data: str):
        self._surname = data
    
    def set_phone(self, data: int):
        self._phone = data
    
    def set_email(self, data: str):
        self._email = data

    def get_name(self):
        return self._name
    
    def get_surname(self):
        return self._surname
    
    def get_phone(self):
        return self._phone
    
    def get_email(self):
        return self._email