class Bike:
  def __init__(ID: int, Is_electric: bool, station_ID, client_ID=None: int):
    self.ID = ID
    self.Is_electric = Is_electric
    self.client_ID = client_ID
    self.time_started = None
    self.station_ID = station_ID
  #атрибути велосипеду(свій вид (електрика/норм), номер, чи взятий якимсь клієнтом разом з ID)

  def start_ride(time):
    self.station_ID = None
    self.time_started = time
  #Метод початку поїздки 

  def end_ride(time, station_ID):
    if Is_electric:
      price = (time - self.time_started) * 5
    else:
      price = (time - self.time_started) * 2
    return price
    #Метод завершує поїздку, вираховує варттість

  def bike_statistic():
    return [self.ID, self.Is_electric, self.client_ID]
      #видає статистику у вигляді списку

  class Station:
    def __init__:
    #атрибути станції(Наявні велосипеди, свій номер/назву)

    def get_available_bikes():
    #Отримати список з наявними велосипедами
      
    def take_bike():
    #Забрати велосипед зі станції

    def return_bike():
    #поставити велосипед зі станції

    def station_statistic():
      #видає статистику у вигляді списку
