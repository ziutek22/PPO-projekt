from database.database_manager import DatabaseManager
from database.car_repository import CarRepository
from database.client_repository import ClientRepository
from database.rental_repository import RentalRepository

from services.car_manager import CarManager
from services.client_manager import ClientManager
from services.rental_manager import RentalManager

from gui.main_window import MainWindow

def build_app():
    db = DatabaseManager("database/rental.db")
    db.connect()
    db.create_tables()

    car_repo = CarRepository(db)
    client_repo = ClientRepository(db)
    rental_repo = RentalRepository(db)

    car_manager = CarManager(car_repo)
    client_manager = ClientManager(client_repo)
    rental_manager = RentalManager(rental_repo, car_repo, client_repo)

    app = MainWindow({
        "car_manager": car_manager,
        "client_manager": client_manager,
        "rental_manager": rental_manager,
    })

    # zamknięcie połączenia przy wyjściu
    def on_close():
        try:
            db.close()
        finally:
            app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_close)
    return app

if __name__ == "__main__":
    app = build_app()
    app.mainloop()
