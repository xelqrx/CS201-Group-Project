class Bike:
  def __init__(self, ID: int, Is_electric: bool, station_ID, client_ID=None):
    self.ID = ID
    self.Is_electric = Is_electric
    self.client_ID = client_ID
    self.time_started = None
    self.station_ID = station_ID
  #атрибути велосипеду(свій вид (електрика/норм), номер, чи взятий якимсь клієнтом разом з ID)

  def start_ride(self, time):
    self.station_ID = None
    self.time_started = time
    
  #Метод початку поїздки 

  def end_ride(self, time, station_ID):
    if Is_electric:
      price = (time - self.time_started) * 5
    else:
      price = (time - self.time_started) * 2
    return price
    #Метод завершує поїздку, вираховує варттість

  def bike_statistic(self):
    return [self.ID, self.Is_electric, self.client_ID]
      #видає статистику у вигляді списку

  class Station:
    def __init__(self, ID, Available_bikes=[]):
      self.ID = ID
      self.Available_bikes = Available_bikes
    #атрибути станції(Наявні велосипеди, свій номер/назву)

    def get_available_bikes(self):
      return self.Available_bikes
    #Отримати список з наявними велосипедами
      
    def take_bike(self, Bike_ID: int):
      bike = self.Available_bikes.pop(Bike_ID)
      return f"{Bike_ID} взяло зі станції {self.ID}"
    #Забрати велосипед зі станції

    def return_bike(self, Bike_ID: int):
      bike = self.Available_bikes.append(Bike_ID)
      return f"{Bike_ID} залишено на станції {self.ID}"
    #поставити велосипед зі станції

    def station_statistic(self):
      return [self.station_ID, self.Available_bikes]
      #видає статистику у вигляді списку
