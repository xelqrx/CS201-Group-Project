from client import Client
from bike_system import Bike
from admin import Admin

Station = Bike.Station

#у завданні сказано що треба щонайменеш 3 поїздки в демо, тому виніс їх в окрему функцію, що бце все не повторювати кілька разів
def make_trip_for_demo(client, bike, start_station, end_station, minutes, admin):
    if len(start_station.get_available_bikes()) == 0:
        return "на станції немає велосипедів"
    if bike.ID not in start_station.get_available_bikes():
        return "цього велосипеда немає на станції"
    if not client.check_balance():
        return "у клієнта мало грошей"

    start_station.Available_bikes.remove(bike.ID)
    bike.start_ride(0)
    client.assign_bike(bike.ID)

    cost = bike.end_ride(minutes, end_station.ID)
    client.balance_change(cost)
    admin.add_revenue(cost)

    end_station.return_bike(bike.ID)
    bike.station_ID = end_station.ID
    client.is_riding = False
    client.bike_id = None
    return cost

#також вивів окремо обробку помилки
def show_result(client, result):
    if isinstance(result, str):
        print(f"ПОМИЛКА: {client.name} не може взяти велосипед - {result}")
    else:
        print(f"Поїздку завершено! Вартість: {result} грн. Залишок у клієнта {client.name}: {client.balance} грн.")


def run_demo_scenario():
    admin = Admin()

    #тут я спочатку не міг зрозуміти через що в нас якось дивно показується кількість велосипедів, виявилося, що у пайтоні, якщо він при створенні у класі має базове значення, то це буде 1 список для всіх об"єктів, тому зараз подаю йому пусті списки
    station_a = Station(1, [])
    station_b = Station(2, [])

    #тут мені підсказали, що можна уточнювати що є що, так як на мене значно зрозуміліше для інших, тому вирішив використати)
    bike1 = Bike(ID=101, Is_electric=False, station_ID=1)
    bike2 = Bike(ID=102, Is_electric=True, station_ID=1)
    bike3 = Bike(ID=103, Is_electric=False, station_ID=2)
    bike4 = Bike(ID=104, Is_electric=True, station_ID=2)

    station_a.return_bike(bike1.ID)
    station_a.return_bike(bike2.ID)
    station_b.return_bike(bike3.ID)
    station_b.return_bike(bike4.ID)

    bikes_db = {
        101: bike1,
        102: bike2,
        103: bike3,
        104: bike4
    }

    olya = Client("Оля", balance=150.0)
    petro = Client("Петро", balance=30.0)

    print("\n--- Початковий стан ---")
    print(f"Клієнт {olya.name} (Баланс): {olya.balance} грн")
    print(f"Клієнт {petro.name} (Баланс): {petro.balance} грн")
    print(f"{station_a.ID} Станція А: велосипеди ID {station_a.get_available_bikes()}")
    print(f"{station_b.ID} Станція Б: велосипеди ID {station_b.get_available_bikes()}")

    print("\n--- Поїздка 1: Оля бере електричний велосипед (102) на Станції 1 ---")
    show_result(olya, make_trip_for_demo(olya, bike2, station_a, station_b, 20, admin))

    print("\n--- Поїздка 2: Петро бере звичайний велосипед (101) на Станції 1 ---")
    show_result(petro, make_trip_for_demo(petro, bike1, station_a, station_b, 10, admin))

    print("\n--- Поїздка 3 (Помилкова дія): Петро пробує взяти велосипед на порожній Станції 1 ---")
    show_result(petro, make_trip_for_demo(petro, bike1, station_a, station_b, 5, admin))

    print("\n--- Поїздка 4: Оля бере звичайний велосипед (103) на Станції 2 ---")
    show_result(olya, make_trip_for_demo(olya, bike3, station_b, station_a, 10, admin))

    print("\n--- Баланс клієнтів після поїздок ---")
    print(f"{olya.name}: {olya.balance} грн")
    print(f"{petro.name}: {petro.balance} грн")

    print()
    print(admin.create_report([station_a, station_b]))

    run_assertions(bikes_db, olya, petro, admin)

#так як я виконував роль 4, то ьс функція для перевірки демо через assert(тут теж трохи поросив ші пояснити як воно працює, бо не знав що таке assert)
def run_assertions(bikes_db, olya, petro, admin):
    assert olya.balance == 30, f"Очікувалося 30 грн, отримано {olya.balance}"
    assert petro.balance == 10, f"Очікувалося 10 грн, отримано {petro.balance}"
    assert admin.balance == 140, f"Очікувалося 140 грн, отримано {admin.balance}"

    b_elec = bikes_db[102]
    b_elec.start_ride(time=10)
    # 30 хв - 10 хв = 20 хв * 5 грн = 100 грн
    cost = b_elec.end_ride(time=30, station_ID=2)
    assert cost == 100, f"Очікувалося 100 грн, отримано {cost}"
    print("\nУсі assert-перевірки успішно пройдено!")

#ну а тут реалізоване головне меню, з якого можна запустити демку
def main():
    stations = []

    progress = True
    while progress:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Запустити демо-сценарій")
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
        else:
            print("Такої дії немає")


if __name__ == "__main__":
    main()
