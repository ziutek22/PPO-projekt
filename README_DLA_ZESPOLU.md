# README – szybkie wprowadzenie do projektu (wersja dla zespołu)

Ten dokument jest napisany prostym językiem, żeby szybko zrozumieć:
- co to za projekt,
- jak działa,
- gdzie są najważniejsze rzeczy w kodzie,
- jakie elementy programowania obiektowego są użyte.

Nie trzeba znać całego projektu na pamięć – to jest mapa.

---

## 1. Co to za projekt

Jest to **desktopowa aplikacja do zarządzania wypożyczalnią samochodów**.

Aplikacja umożliwia:
- dodawanie samochodów,
- dodawanie klientów,
- tworzenie wypożyczeń,
- automatyczne liczenie kosztu wypożyczenia,
- zapisywanie wszystkiego w bazie danych.

---

## 2. W jakich technologiach to jest zrobione i dlaczego

### Python
- Główny język projektu.
- Czytelny i prosty do pisania OOP.
- Dobrze nadaje się do projektów studenckich.

### tkinter (GUI)
- Wbudowana biblioteka Pythona.
- Nie trzeba instalować nic dodatkowego.
- Służy do tworzenia okien, formularzy i tabel.

### SQLite (baza danych)
- Baza danych w jednym pliku.
- Nie wymaga serwera ani konfiguracji.
- Idealna do małych aplikacji desktopowych.

---

## 3. Jak działa aplikacja (logika w skrócie)

Schemat działania:

GUI → services → database → SQLite

1. Użytkownik klika coś w GUI (np. „Dodaj samochód”)
2. GUI przekazuje dane do klasy z folderu `services`
3. `services`:
   - sprawdzają poprawność danych (walidacja)
   - wykonują logikę (np. liczenie ceny)
4. Dane są zapisywane do bazy przez klasy z `database`
5. Wynik wraca do GUI i jest pokazany użytkownikowi

GUI **nie zawiera logiki biznesowej** – tylko obsługę interfejsu.

---

## 4. Mechanizm bazy danych – jak to działa

- Baza danych to plik SQLite.
- Tworzona automatycznie przy starcie aplikacji.
- Tabele:
  - `cars`
  - `clients`
  - `rentals`

### Folder `database`
- `database_manager.py` – łączy się z bazą, wykonuje SQL
- `*_repository.py` – konkretne operacje na tabelach (CRUD)

Kod GUI **nie używa SQL bezpośrednio**.

---

## 5. Programowanie obiektowe – gdzie co jest

### Klasy i obiekty
- Każdy główny element systemu to klasa:
  - `Car`
  - `Client`
  - `Rental`
- Obiekty tych klas reprezentują realne byty (samochód, klient, wypożyczenie).

Pliki: `models/`

---

### Hermetyzacja
- Dane obiektów są przechowywane jako pola klasy.
- Dostęp do nich odbywa się przez metody (gettery/settery lub metody logiczne).
- Logika nie jest rozrzucona po całym projekcie.

---

### Konstruktory
- Każda klasa modelu ma konstruktor `__init__`.
- Konstruktor ustawia początkowy stan obiektu.

Przykład:
- samochód ma markę, model, rok, cenę itd. ustawione przy tworzeniu obiektu.

---

### Dziedziczenie
- `Car` dziedziczy po `Vehicle`.

`Vehicle`:
- marka
- model
- rok

`Car`:
- wszystko z `Vehicle`
- + numer rejestracyjny
- + cena
- + dostępność

Pliki:
- `models/vehicle.py`
- `models/car.py`

---

### Interfejsy
- W projekcie **nie są aktywnie używane** w uproszczonej wersji.
- Były rozważane, ale usunięte dla prostoty i czytelności.

---

### Klasy abstrakcyjne
- **Nie są używane**.
- Projekt celowo jest prosty i na poziomie studenckim.

---

### Funkcje anonimowe (lambda)
- **Nie są używane**.
- Projekt nie wymagał ich zastosowania.

---

### Wyjątki
- Wyjątki są używane minimalnie.
- Błędy walidacji są obsługiwane głównie przez:
  - sprawdzanie warunków (`if`)
  - zwracanie komunikatów do GUI
- Dzięki temu kod jest prostszy do zrozumienia.

---

### Refleksja
- **Nie jest używana**.
- Projekt nie korzysta z dynamicznego sprawdzania klas czy metod.

---

## 6. Co warto zapamiętać na szybko

- GUI = tylko okna i przyciski
- `services` = cała logika
- `database` = SQL i zapis danych
- `models` = klasy obiektów
- Projekt jest prosty celowo – pod zaliczenie i OOP

---

## 7. Jak odpalić projekt
```bash
python main.py
```

I to wszystko 🙂  
Ten README wystarcza, żeby szybko ogarnąć projekt i o nim opowiedzieć.
