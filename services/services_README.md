## Folder `services`

Folder zawiera warstwę logiki biznesowej aplikacji. Klasy w tym folderze pośredniczą między GUI a warstwą bazy danych, wykonują walidacje i kontrolują poprawność operacji.

### `car_manager.py`
- Logika zarządzania samochodami.
- Walidacja danych auta (marka, model, rok, cena, rejestracja).
- Dodawanie, edycja, usuwanie samochodów.
- Zmiana dostępności samochodu.

### `client_manager.py`
- Logika zarządzania klientami.
- Walidacja danych klienta (imię, nazwisko, telefon, email).
- Dodawanie i usuwanie klientów.
- Pobieranie listy klientów.

### `rental_manager.py`
- Logika tworzenia wypożyczeń.
- Walidacja dat (format, zakres, brak dat w przeszłości).
- Sprawdzenie dostępności samochodu.
- Wyliczanie kosztu wypożyczenia.
- Zmiana dostępności auta po wypożyczeniu.
