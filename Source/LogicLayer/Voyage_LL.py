from models.Voyage import Voyage
from models.Destination import Destination
from models.Airplane import Airplane
from DataLayer.Get_DL import Get_DL
from utils.print_functions import *
import dateutil.parser
import datetime
import time

class VoyageLL:
    '''Logic Layer Voyage Class

        Logic layer classes receive information from the LLAPI class for processing.
        Information is passed on to IOAPI which interacts with data layer classes.

    '''

    def __init__(self, dapi_in):
        self.__voyage_repo = dapi_in 
        self.__voyage = Voyage()
        self.__get = Get_DL()

    def add_voyage(self, voyage):
        '''Takes in input information about a new voyage. Calculates the necessary
           dates and times. Forwards all information to the Data layer.'''
        if self.is_valid_voyage(voyage):
            get_destination = voyage.destination
            destination = self.__get.get_destination_by_airport_class(get_destination)

            voyage.arrival_at_dest = self.calculate_time(voyage.departure, destination.duration)
            voyage.departure_from_dest = self.calculate_time(voyage.arrival_at_dest, "01:00")
            voyage.arrival_back_home = self.calculate_time(voyage.departure_from_dest, destination.duration)

            parseDate_dep = dateutil.parser.parse(voyage.departure)
            dep_year, dep_month, dep_day = parseDate_dep.year, parseDate_dep.month, parseDate_dep.day

            voyage.flight_out, voyage.flight_in = self.generate_flight_number(voyage.destination, dep_year, dep_month, dep_day)

            self.__voyage_repo.add_voyage(voyage)

    def is_valid_voyage(self, voyage):
        return True
    
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__voyage_repo.get_voyage_destination(voyage_destination, year_int, month_int, day_int)

    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__voyage_repo.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)

    def get_all_voyage_at_date(self, year_int, month_int, day_int):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__voyage_repo.get_all_voyage_at_date(year_int, month_int, day_int)

    def parse_date(self, departure_time):
        '''Takes in a date in isoformat and parses it to be able to use the date
           in calculations.'''
        voyage_departure = dateutil.parser.parse(self.__voyage.departure)
        voyage_year = voyage_departure.year
        voyage_month = voyage_departure.month_int
        voyage_day = voyage_departure.day
        voyage_hh = voyage_departure.hour
        voyage_mm = voyage_departure.minute
        return voyage_year, voyage_month, voyage_day, voyage_hh, voyage_mm

    def calculate_time(self, start_time, duration):
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

    
    def get_voyage_airport(self):
        '''Takes no input. Talks to the Data layer and gets an instance of 
           a destination based on a specific voyage. Returns the instance of
           the destination to the UI layer.'''
        airport_str = input("Please enter airport: ")
        while not(self.airport_is_valid(airport_str)):
            print("Please insert a valid airport from the list.")
            airport_str = input("Please enter airport: ")          
        else:
            return airport_str
        
    def airport_is_valid(self, airport):
        '''Check function to see if a valid destination airport has been inputed.'''
        destinations = self.__get.get_destination()
        return any(destination.airport == airport for destination in destinations)

    def get_voyage_airplane(self, plane_list):
        '''Takes in an airplane list. If input is valid it forwards it to the
           Data layer which fetches the necessary data and returns it back
           to the UI layer.'''
        airplanes_list = plane_list
        air_input = 0
        while air_input != 1:
            airplane_str = input("Airplane (name): ")
            if airplane_str not in airplanes_list:
                print("Wrong input or airplane not available")
                print("Please choose an airplane from the list")
            else:
                air_input = 1
                return airplane_str

    def get_voyage_date(self):
        '''Asks for input for a date and validates the input format and
           values.'''
        while True:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date_list = date_str.split("-")
            try:
                time.strptime(date_str, '%Y-%m-%d')
                return date_list
            except ValueError:
                print("Invalid format. Please enter a valid date")

    def get_voyage_time(self):
        '''Asks for input for a time and validates the input format and
           values.'''
        print("Departure time (Departures from Iceland are between 08:00 and 19:45 (including both)")
        print("four departure times per hour, on minutes 00, 15, 30, and 45)")
        HOURS = ["08","09","10","11","12","13","14","15","16","17","18","19"]
        MINUTES = ["00","15","30","45"]
        check = False
        while not check:
            time_str = input("Enter departure time (hh:mm): ")
            time_list = time_str.split(":")
            if len(str(time_list[0])) == 2 and len(str(time_list[1])) == 2:
                if time_list[0] in HOURS:
                    if time_list[1] in MINUTES:
                        return time_list
            else:
                print("Invalid format. Please enter a valid time")
    
    def generate_flight_number(self, destination, voyage_year, voyage_month, voyage_day):
        '''Takes in a destination and a date. Based on the information the function
           generates a flight number bot for flight from Iceland and back to Iceland.
           Follows the rules given for the flight numbers.'''
        voyage_on_the_day = self.__get.get_voyage_destination(destination, voyage_year, voyage_month, voyage_day)
        destination_lst = self.__get.get_destination()
        dest_number_str = ""
        for index, item in enumerate(destination_lst):
            if destination == item.airport:
                dest_number_int = index + 1
                if dest_number_int < 10:
                    dest_number_str += "0" + str(dest_number_int)
                else:
                    dest_number_str += str(dest_number_int)

            flight_extention_out = (len(voyage_on_the_day)) * 2
            flight_extention_home = ((len(voyage_on_the_day)) * 2) + 1

            flight_number_out = "NA" + dest_number_str + str(flight_extention_out)
            flight_number_home = "NA" + dest_number_str + str(flight_extention_home)

        return flight_number_out, flight_number_home

    def get_flight_number(self, destination, year, month, day):
        '''Assignes the flight number to the Voyage class.'''
        while True:
            flight_number = input("Please insert flight number for the voyage: ").upper()
            the_voyage = self.get_the_voyage(destination, int(year), int(month), int(day), flight_number)
            if the_voyage != []:
                return (the_voyage)                
            else:
                print("Wrong flight number. Please try again.")


    def update_voyage(self, the_voyage, captain_str, pilot_str, fsm_str, fa_str):
        '''Takes call from the UI layer and send it to the Data layer
           so the data can be written to the Data layer.'''
        return self.__voyage_repo.update_voyage(the_voyage, captain_str, pilot_str, fsm_str, fa_str)