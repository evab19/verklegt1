from models.Voyage import Voyage
from models.Destination import Destination
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

            parseDate = dateutil.parser.parse(voyage.departure)
            dep_year, dep_month, dep_day, dep_hour, dep_min = parseDate.year, parseDate.month, parseDate.day, parseDate.hour, parseDate.minute
            flight_time_hours, flight_time_min = destination.duration.split(':')
            flight_time_hours = int(flight_time_hours)
            flight_time_min = int(flight_time_min)

            if dep_min + flight_time_min >= 60:
                arrival_time_hour = dep_hour + flight_time_hours + 1
                arrival_time_min = dep_min + flight_time_min - 60
            else:
                arrival_time_hour = dep_hour + flight_time_hours
                arrival_time_min = dep_min + flight_time_min

            voyage.arrival_at_dest = datetime.datetime(dep_year, dep_month, dep_day, arrival_time_hour, arrival_time_min, 0).isoformat()
            self.__voyage_repo.add_voyage(voyage)

    def is_valid_voyage(self, __voyage):
        #add code here to verify
        return True
    
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        return self.__voyage_repo.get_voyage_destination(voyage_destination, year_int, month_int, day_int)

    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        return self.__voyage_repo.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)

    def parse_date(self, departure_time):
        voyage_departure = dateutil.parser.parse(self.__voyage.departure)
        voyage_year = voyage_departure.year
        voyage_month = voyage_departure.month_int
        voyage_day = voyage_departure.day
        voyage_hh = voyage_departure.hour
        voyage_mm = voyage_departure.minute
        return voyage_year, voyage_month, voyage_day, voyage_hh, voyage_mm
