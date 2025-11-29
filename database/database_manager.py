import sqlite3

class DatabaseManager:
    def __init__(self, dbPath = "rental.db"):
        self._dbPath = dbPath
        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = sqlite3.connect(self._dbPath)
        self._cursor = self._connection.cursor()
        return self._connection
    
    def create_tables(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,surname TEXT NOT NULL,phone TEXT NOT NULL UNIQUE,email TEXT)")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS cars ( id INTEGER PRIMARY KEY AUTOINCREMENT, brand TEXT NOT NULL, model TEXT NOT NULL, productionYear INTEGER NOT NULL, fuelType TEXT NOT NULL, price REAL NOT NULL, plates TEXT NOT NULL,isAvailable INTEGER NOT NULL CHECK (isAvailable IN (0,1)));")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS rentals ( id INTEGER PRIMARY KEY AUTOINCREMENT, client_id INTEGER NOT NULL, car_id INTEGER NOT NULL, rentDate TEXT NOT NULL, returnDate TEXT NOT NULL, FOREIGN KEY (client_id) REFERENCES clients(id), FOREIGN KEY (car_id) REFERENCES cars(id));")
        self._connection.commit()

    def execute(self, query, params = ()):
        self._cursor.execute(query, params)
        self._connection.commit()
        return self._cursor


    def fetch_all(self, query, params =  ()):
        self._cursor.execute(query, params)
        result = self._cursor.fetchall()
        return result

    def fetch_one(self, query, params = ()):
        self._cursor.execute(query, params)
        result = self._cursor.fetchone()
        return result 
