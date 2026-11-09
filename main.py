from client import Client
from bike_system import Bike

Station = Bike.Station

from admin import Admin


def run_demo_scenario():
    admin = Admin()

    station_a = Station(ID=1, Available_bikes=[])
    station_b = Station(ID=2, Available_bikes=[])

    bike1 = Bike(ID=101, Is_electric=False, station_ID=1)
    bike2 = Bike(ID=102, Is_electric=True, station_ID=1)
    bike3 = Bike(ID=103, Is_electric=False, station_ID=2)
    bike4 = Bike(ID=104, Is_electric=True, station_ID=2)

    station_a.Available_bikes.extend([bike1.ID, bike2.ID])
    station_b.Available_bikes.extend([bike3.ID, bike4.ID])

    bikes_db = {
        101: bike1,
        102: bike2,
        103: bike3,
        104: bike4
    }

    olya = Client("Оля", balance=150.0)
    petro = Client("Петро", balance=30.0)

    print("\n--- Початковий стан ---")
    print(f"Клієнт {olya.balance} (Баланс): {olya.balance} грн")
    print(f"{station_a.ID} Станція А: велосипеди ID {Station.get_available_bikes(station_a)}")
    print(f"{station_b.ID} Станція Б: велосипеди ID {Station.get_available_bikes(station_b)}")

    print("\n--- Поїздка 1: Оля бере електричний велосипед (102) на Станції 1 ---")
    avail_a = Station.get_available_bikes(station_a)
    if 102 in avail_a:
        station_a.Available_bikes.remove(102)
        bike_obj = bikes_db[102]

        Bike.start_ride(bike_obj, time=0)
        olya.is_riding = True

        trip_cost = Bike.end_ride(bike_obj, time=20, station_ID=2)

        olya.balance -= trip_cost
        olya.is_riding = False
        Station.return_bike(station_b, bike_obj.ID)
        admin.balance += trip_cost

        print(f"Поїздку завершено! Тривалість: 20 хв. Вартість: {trip_cost} грн.")
        print(f"Залишок у Олі: {olya.balance} грн. Баланс мережі: {admin.balance} грн.")

    print("\n--- Поїздка 2 (Помилкова дія): Спроба забрати велик з порожньої станції ---")
    empty_station = Station(ID=99, Available_bikes=[])

    if not Station.get_available_bikes(empty_station):
        print("ПОМИЛКА: На станції 99 немає доступних велосипедів!")

    print("\n" + "=" * 60)
    print("ЗВІТ АДМІНІСТРАТОРА")
    print("=" * 60)
    admin.create_report([station_a, station_b])

    run_assertions(bikes_db)


def run_assertions(bikes_db):
    b_elec = bikes_db[102]
    Bike.start_ride(b_elec, time=10)
    # 30 хв - 10 хв = 20 хв * 5 грн = 100 грн
    cost = Bike.end_ride(b_elec, time=30, station_ID=2)
    assert cost == 100, f"Очікувалося 100 грн, отримано {cost}"
    print("\nУсі assert-перевірки успішно пройдено!")


def main():
    stations = []

    progress = True
    while progress:
        print("\n--- ГОЛОВНЕ МЕНЮ (bike_system_2 / client_2) ---")
        print("1. Запустити адаптований Демо-сценарій")
        print("2. Створити станцію")
        print("0. Вийти")

        cmd = input("Виберіть дію: ").strip()
        if cmd == "1":
            run_demo_scenario()
        elif cmd == "2":
            st_id = len(stations) + 1
            st = Station(ID=st_id, Available_bikes=[])
            stations.append(st)
            print(f"Станцію з ID={st_id} створено!")
        elif cmd == "0":
            progress = False


if __name__ == "__main__":
    main()
