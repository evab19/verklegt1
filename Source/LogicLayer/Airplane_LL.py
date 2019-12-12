from models.Airplane import Airplane
import dateutil.parser
import datetime
import time

class AirplaneLL:

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, airplane):
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
     
    def is_valid_airplane(self, __airplane):
        if __airplane.name and __airplane.model and __airplane.producer and __airplane.number_of_seats:
            return True
        else:
            return False
 
    def get_airplane(self, year_int, month_int, day_int, hour_int, min_int):
        our_airplanes = self.__airplane_repo.get_airplane()
        our_airplanes = self.get_airplane_status(year_int, month_int, day_int, hour_int, min_int, our_airplanes)
        # for plane in our_airplanes:
        #     for a_planes in available_planes:
        #         if plane.name == a_planes.name:
        #             plane.plane_status = "A"
        #             break
        #         else:
        #             plane.plane_status = "B"
        return our_airplanes

    def get_airplanes(self):
        our_airplanes = self.__airplane_repo.get_airplane()
        return our_airplanes

    def get_airplane_status(self, year_int, month_int, day_int, hour_int, min_int, our_airplanes):
        the_airplanes = our_airplanes

        voyages_at_same_date = self.__airplane_repo.get_all_voyage_at_date(year_int, month_int, day_int)
        
        #time_now_str = str(year_int) + str(month_int) + str(day_int) + str(hour_int) + str(min_int)
        time_now = datetime.datetime(year_int, month_int, day_int, hour_int, min_int, 0).isoformat()

        for plane in the_airplanes:
            for voyage in voyages_at_same_date:
                if plane.name == voyage.airplane:
                    #times of voyage
                    departure_time = voyage.departure
                    landed_at_destination_time = self.calculate_time_airplane(departure_time, "0:00")
                    departure_from_destination_time = self.calculate_time_airplane(landed_at_destination_time, "0:02")
                    landed_at_home_time = self.calculate_time_airplane(departure_from_destination_time, "0:00")

                    if ((time_now < departure_time) or (time_now > landed_at_home_time)):
                        plane.plane_status = "A (SLTD)"
                    elif ((time_now >= departure_time) and (time_now < landed_at_destination_time)):
                        plane.plane_status = "I (outward)"
                    elif ((time_now >= landed_at_destination_time) and (time_now < departure_from_destination_time)):
                        plane.plane_status = "LA"
                    elif ((time_now >= departure_from_destination_time) and (time_now < landed_at_home_time)):
                        plane.plane_status = "I (inward)"
                    else:
                        plane.plane_status = "A"
        
        return the_airplanes
                    


    def parse_date_airplane(self, departure_time):
        voyage_departure = dateutil.parser.parse(self.__voyage.departure)
        voyage_year = voyage_departure.year
        voyage_month = voyage_departure.month_int
        voyage_day = voyage_departure.day
        voyage_hh = voyage_departure.hour
        voyage_mm = voyage_departure.minute
        return voyage_year, voyage_month, voyage_day, voyage_hh, voyage_mm

    def calculate_time_airplane(self, start_time, duration):
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
        airplanes = self.get_airplanes()
        return any(airplane.model == model for airplane in airplanes)
