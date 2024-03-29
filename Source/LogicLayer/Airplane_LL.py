from models.Airplane import Airplane
import dateutil.parser
import datetime
import time

class AirplaneLL:
    '''Logic Layer Airplane Class
       --------------------------

        Logic layer classes receive information from the LLAPI class for processing.
        Information is passed on to IOAPI which interacts with data layer classes

    '''

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, airplane):
        '''Takes an input from the UI layer and sends it to the Data layer to be saved 
           to the database.'''
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
     
    def is_valid_airplane(self, __airplane):
        '''Takes in an instance of an airplane and validates it. If OK returns True, else False.'''
        if __airplane.name and __airplane.model and __airplane.producer and __airplane.number_of_seats:
            return True
        else:
            return False
 
    def get_airplane(self, year_int, month_int, day_int, hour_int, min_int):
        our_airplanes = self.__airplane_repo.get_airplane()
        our_airplanes = self.get_airplane_status(year_int, month_int, day_int, hour_int, min_int, our_airplanes)
        return our_airplanes

    def get_airplanes(self):
        '''Takes in no input. Calls the Data layer which returns all airplanes from the 
           airplanes.csv file. Sends it back to the UI layer.'''
        our_airplanes = self.__airplane_repo.get_airplane()
        return our_airplanes

    def get_airplane_status(self, year_int, month_int, day_int, hour_int, min_int, our_airplanes):
        the_airplanes = our_airplanes

        voyages_at_same_date = self.__airplane_repo.get_all_voyage_at_date(year_int, month_int, day_int)
        
        time_now = datetime.datetime(year_int, month_int, day_int, hour_int, min_int, 0).isoformat()

        for plane in the_airplanes:
            for voyage in voyages_at_same_date:
                if plane.name == voyage.airplane:
                    voyage_destination = self.__airplane_repo.get_destination_by_airport_class(voyage.destination)
                    departure_time = voyage.departure
                    landed_at_destination_time = self.calculate_time_airplane(departure_time, voyage_destination.duration)
                    departure_from_destination_time = self.calculate_time_airplane(landed_at_destination_time, "1:00")
                    landed_at_home_time = self.calculate_time_airplane(departure_from_destination_time, voyage_destination.duration)

                    if ((time_now < departure_time)):
                        plane.plane_status = "Booked today"
                    elif ((time_now >= departure_time) and (time_now < landed_at_destination_time)):
                        plane.plane_status = "In air outbound"
                    elif ((time_now >= landed_at_destination_time) and (time_now < departure_from_destination_time)):
                        plane.plane_status = "Landed abroad"
                    elif ((time_now >= departure_from_destination_time) and (time_now < landed_at_home_time)):
                        plane.plane_status = "In air inbound"
                    else:
                        plane.plane_status = "Available"
        
        return the_airplanes
        

    def parse_date_airplane(self, departure_time):
        '''Takes in a date in isoformat and parses it to be able to use the date
           in calculations.'''
        voyage_departure = dateutil.parser.parse(self.__voyage.departure)
        voyage_year = voyage_departure.year
        voyage_month = voyage_departure.month_int
        voyage_day = voyage_departure.day
        voyage_hh = voyage_departure.hour
        voyage_mm = voyage_departure.minute
        return voyage_year, voyage_month, voyage_day, voyage_hh, voyage_mm

    def calculate_time_airplane(self, start_time, duration):
        '''Takes in a date and time string, and duration string. Uses the parse
           function to parse it and then calculates a new time and returns it'''
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

    def get_airplane_model(self, status = ""):
        if status == "update":
            model = input("Choose airplane model licence: ")
            if model == "":
                return model
            else:
                while True:
                    if self.check_model(model):
                        return model
                    else:
                        print("Invalid input. Please choose a model from the list")
                        model = input("Choose airplane model licence: ")
        else:
            while True:
                model = input("Choose airplane model licence: ")
                if self.check_model(model):
                    return model
                else:
                    print("Invalid input. Please choose a model from the list")

    def check_model(self, model):
        '''Takes in an airplane model and checks to see if it is valid.'''
        airplanes = self.get_airplanes()
        return any(airplane.model == model for airplane in airplanes)

    def is_airplane_unique(self, name_str):
        '''Takes in an airplane name and checks to see if there already is
           an airplane with that name in the system.'''
        airplanes = self.get_airplanes()
        return not(any(airplane.name.lower() == name_str.lower() for airplane in airplanes))