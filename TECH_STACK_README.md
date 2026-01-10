## Stack technologiczny projektu

Projekt został zrealizowany jako desktopowa aplikacja w języku Python, z prostą architekturą warstwową dostosowaną do poziomu zajęć z programowania obiektowego.

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

### Warstwa dostępu do danych (repository)
- Klasy w folderze `database`.
- Odpowiadają za komunikację z bazą danych.
- Oddzielają logikę SQL od reszty aplikacji.

### Warstwa logiki biznesowej (services)
- Klasy w folderze `services`.
- Zawierają:
  - walidację danych,
  - zasady działania wypożyczeń,
  - obliczanie kosztów.
- Dzięki temu GUI nie zawiera logiki biznesowej.

### Modele danych (models)
- Klasy reprezentujące encje systemu:
  - samochód,
  - klient,
  - wypożyczenie.
- Przechowują dane i podstawowe zachowania obiektów.

### Architektura
- Prosta architektura warstwowa:
  - GUI → Services → Database
- Ułatwia czytanie kodu i jego rozbudowę.
- Dopasowana do poziomu projektu studenckiego.
