class Client:
    def __init__(self, name: str, surname: str, phone: str, email: str | None = None):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._email = email

    def set_name(self, name: str) -> None:
        self._name = name

    def set_surname(self, surname: str) -> None:
        self._surname = surname

    def set_phone(self, phone: str) -> None:
        self._phone = phone

    def set_email(self, email: str | None) -> None:
        self._email = email

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_phone(self) -> str:
        return self._phone

    def get_email(self) -> str | None:
        return self._email
