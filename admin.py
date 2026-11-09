class Admin:
    def __init__(self):
        self.balance = 0.0

    def add_revenue(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def create_report(self, stations_list: list) -> str:
        lines = []
        #додав трохи декору, надихаючись однією з перших практичних що робив у КШЕ)
        lines.append("=" * 45)
        lines.append("ЗВІТ АДМІНІСТРАТОРА ПРО СТАН МЕРЕЖІ")
        lines.append("=" * 45)

        total_bikes_in_network = 0

        if not stations_list:
            lines.append("Наразі в мережі немає зареєстрованих станцій.")
        else:
            lines.append("Станції та велосипеди:")
            for station in stations_list:
                bike_count = len(station.get_available_bikes())
                total_bikes_in_network += bike_count

                lines.append(f"  • Станція [{station.ID}]: {bike_count} велосипедів")

        lines.append(f"Всього велосипедів на станціях: {total_bikes_in_network}")
        lines.append(f"Загальний заробіток мережі: {self.balance:.2f} грн")

        report_text = "\n".join(lines)
        return report_text
