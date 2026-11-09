class Admin:
    def __init__(self):
        self.balance = 0.0

    def add_revenue(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def create_report(self, stations_list: list) -> str:
        lines = []
        lines.append("=" * 45)
        lines.append("ЗВІТ АДМІНІСТРАТОРА ПРО СТАН МЕРЕЖІ")
        lines.append("=" * 45)

        total_bikes_in_network = 0

        if not stations_list:
            lines.append("⚠Наразі в мережі немає зареєстрованих станцій.")
        else:
            lines.append("Станції та велосипеди:")
            for station in stations_list:
                st_id = getattr(station, "name", None) or getattr(station, "ID", None) or getattr(station, "station_id",
                                                                                                  "Невідома")

                if hasattr(station, "get_available_bikes"):
                    bikes = station.get_available_bikes()
                elif hasattr(station, "Available_bikes"):
                    bikes = station.Available_bikes
                elif hasattr(station, "bikes"):
                    bikes = station.bikes
                else:
                    bikes = []

                bike_count = len(bikes) if isinstance(bikes, list) else 0
                total_bikes_in_network += bike_count

                lines.append(f"  • Станція [{st_id}]: {bike_count} велосипедів")

        lines.append("-" * 45)
        lines.append(f"Всього велосипедів на станціях: {total_bikes_in_network}")
        lines.append(f"Загальний заробіток мережі: {self.balance:.2f} грн")
        lines.append("=" * 45)

        report_text = "\n".join(lines)
        print(report_text)
        return report_text
