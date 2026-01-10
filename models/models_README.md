## Folder `models`

Folder zawiera klasy modelowe aplikacji. Reprezentują one główne encje systemu i przechowują dane oraz podstawową logikę związaną z obiektami.

### `vehicle.py`
- Klasa bazowa dla pojazdów.
- Przechowuje wspólne dane: marka, model, rok produkcji.

### `car.py`
- Reprezentuje samochód dostępny w wypożyczalni.
- Rozszerza `Vehicle`.
- Przechowuje m.in. numer rejestracyjny, cenę za dzień, paliwo oraz dostępność.

### `client.py`
- Reprezentuje klienta wypożyczalni.
- Przechowuje dane osobowe: imię, nazwisko, telefon, email.

### `rental.py`
- Reprezentuje pojedyncze wypożyczenie.
- Łączy klienta z samochodem.
- Przechowuje daty wypożyczenia oraz całkowity koszt.
