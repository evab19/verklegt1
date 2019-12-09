from models.Voyage import Voyage
from models.Destination import Destination
from models.Airplane import Airplane
from DataLayer.Get_DL import Get_DL
import dateutil.parser
import datetime

class VoyageLL:

    def __init__(self, dapi_in):
        self.__voyage_repo = dapi_in 
        self.__voyage = Voyage()
        self.__get = Get_DL()

    def add_voyage(self, voyage):
        if self.is_valid_voyage(voyage):
            get_destination = voyage.destination
            destination = self.__get.get_destination_by_airport_class(get_destination)

            voyage.arrival_at_dest = self.calculate_time(voyage.departure, destination.duration)
            voyage.departure_from_dest = self.calculate_time(voyage.arrival_at_dest, "01:00")
            voyage.arrival_back_home = self.calculate_time(voyage.departure_from_dest, destination.duration)

            self.__voyage_repo.add_voyage(voyage)

    def is_valid_voyage(self, voyage):
        #add code here to verify
        return True
    
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        return self.__voyage_repo.get_voyage_destination(voyage_destination, year_int, month_int, day_int)

    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        return self.__voyage_repo.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)

    def get_all_voyage_at_date(self, year_int, month_int, day_int):
        return self.__voyage_repo.get_all_voyage_at_date(year_int, month_int, day_int)

    def parse_date(self, departure_time):
        voyage_departure = dateutil.parser.parse(self.__voyage.departure)
        voyage_year = voyage_departure.year
        voyage_month = voyage_departure.month_int
        voyage_day = voyage_departure.day
        voyage_hh = voyage_departure.hour
        voyage_mm = voyage_departure.minute
        return voyage_year, voyage_month, voyage_day, voyage_hh, voyage_mm

    def calculate_time(self, start_time, duration):
        parseDate = dateutil.parser.parse(start_time)
        dep_year, dep_month, dep_day, dep_hour, dep_min = parseDate.year, parseDate.month, parseDate.day, parseDate.hour, parseDate.minute
        flight_time_hours, flight_time_min = duration.split(':')
        flight_time_hours = int(flight_time_hours)
        flight_time_min = int(flight_time_min)

        if dep_min + flight_time_min >= 60:
            arrival_time_hour = dep_hour + flight_time_hours + 1
            arrival_time_min = dep_min + flight_time_min - 60
        else:
            arrival_time_hour = dep_hour + flight_time_hours
            arrival_time_min = dep_min + flight_time_min
        
        if arrival_time_hour >= 24:
            arrival_time_hour -= 24
            dep_day += 1
        
        if dep_month in [4, 6, 9, 11]:
            if dep_day > 30:
                dep_month += 1
                dep_day -= 30
        elif dep_month == 2:
            if dep_day > 28:
                dep_month += 1
                dep_day -= 28
        elif dep_month in [1, 3, 5, 7, 8, 10]:
            if dep_day > 31:
                dep_month += 1
                dep_day -= 31
        elif dep_month == 12:
            if dep_day > 31:
                dep_month = 1
                dep_day -= 31
                dep_year += 1

        new_time = datetime.datetime(dep_year, dep_month, dep_day, arrival_time_hour, arrival_time_min, 0).isoformat()
        return new_time

    