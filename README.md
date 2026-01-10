# PPO-projekt – Wypożyczalnia samochodów (Python + SQLite + Tkinter)

## Co to jest
Prosta aplikacja okienkowa wypożyczalni samochodów. Pozwala:
- dodać/edytować/usunąć samochody i zmieniać ich dostępność,
- dodać/usunąć klientów,
- utworzyć wypożyczenie (tylko dla dostępnego auta) i policzyć cenę.

Dane są zapisywane w SQLite: `database/rental.db`.

### Język programowania – Python
- Główny język całego projektu.
- Wybrany ze względu na:
  - prostą składnię,
  - czytelność kodu,
  - dobre wsparcie dla programowania obiektowego,
  - dostępność bibliotek do GUI i baz danych.

### Interfejs graficzny (GUI) – tkinter
- Wbudowana biblioteka Pythona do tworzenia aplikacji okienkowych.
- Użyta, ponieważ:
  - nie wymaga instalowania dodatkowych bibliotek,
  - jest wystarczająca do prostych formularzy i tabel,
  - dobrze nadaje się do projektów zaliczeniowych.

### Baza danych – SQLite
- Lekka, plikowa baza danych.
- Użyta, ponieważ:
  - nie wymaga instalacji serwera,
  - zapis danych odbywa się w jednym pliku,
  - idealnie nadaje się do małych aplikacji desktopowych.

## Jak uruchomić
1. Python 3.10+.
2. W folderze projektu uruchom:
- Windows: `python main.py`
- Linux/macOS: `python3 main.py`

Jeśli na Linux brakuje Tkinter: `sudo apt install python3-tk`

## Jak to działa (w skrócie)
1. `main.py`
- łączy się z bazą (`DatabaseManager`),
- tworzy tabele jeśli ich nie ma,
- tworzy repozytoria i managery,
- uruchamia GUI.

2. `gui/` (okna)
- wyświetla formularze i tabelki,
- po kliknięciu przycisku wywołuje metody managerów,
- pokazuje komunikaty (OK / błąd).

3. `services/` (managery)
- robią walidacje danych (np. rok, cena, telefon, daty),
- wywołują metody repozytoriów,
- zwracają wynik w prostym formacie: `(True/False, komunikat)`.

4. `database/` (repozytoria)
- wykonują zapytania SQL (INSERT/SELECT/UPDATE/DELETE),
- zapisują i odczytują dane z SQLite.

## Zasady wypożyczeń
- samochód musi być dostępny (`available = 1`),
- daty muszą być w formacie `YYYY-MM-DD`,
- nie da się dodać wypożyczenia w przeszłości (start < dzisiaj),
- cena = liczba dni * cena za dzień,
- po dodaniu wypożyczenia auto jest ustawiane na niedostępne.

## Struktura folderów
- `models/` – klasy obiektów (Car, Client, Rental, Vehicle)
- `database/` – SQLite + repozytoria
- `services/` – logika + walidacje
- `gui/` – okna Tkinter
