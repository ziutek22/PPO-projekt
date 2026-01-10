## Folder `database`

Folder zawiera warstwę dostępu do danych (SQLite). Odpowiada za połączenie z bazą, tworzenie tabel oraz operacje CRUD na encjach.

### `database_manager.py`
- Zarządza połączeniem z bazą SQLite.
- Tworzy tabele przy starcie aplikacji.
- Udostępnia metody do wykonywania zapytań SQL (`execute`, `fetch_one`, `fetch_all`).

### `car_repository.py`
- Operacje na tabeli `cars`.
- Dodawanie, pobieranie, aktualizacja i usuwanie samochodów.
- Zmiana dostępności samochodu.

### `client_repository.py`
- Operacje na tabeli `clients`.
- Dodawanie, pobieranie i usuwanie klientów.
- Wyszukiwanie klienta po numerze telefonu.

### `rental_repository.py`
- Operacje na tabeli `rentals`.
- Dodawanie wypożyczeń.
- Pobieranie listy wypożyczeń (z danymi klienta i samochodu).

### `rental.sql`
- Definicja struktury tabeli `rentals`.
- Dokumentacja schematu bazy danych.
