from models.Airplane import Airplane
from datetime import date

class AirplaneLL:

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, airplane):
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
     
    def is_valid_airplane(self, __airplane):
        if __airplane.name and __airplane.model and __airplane.producer and __airplane.number_of_seats and __airplane.status != "":
            return True
        else:
            return False
 
    def get_airplane(self):
        our_airplanes = self.__airplane_repo.get_airplane()
        today = date.today()
        available_planes = self.get_airplane_status(today.year, today.month, today.day)
        for plane in our_airplanes:
            for a_planes in available_planes:
                if plane.name == a_planes.name:
                    plane.plane_status = "A"
                    break
                else:
                    plane.plane_status = "B"
        return our_airplanes

    def get_airplane_status(self, year_int, month_int, day_int):
        airplanes = self.__airplane_repo.get_airplane()
        voyages_at_same_date = self.__airplane_repo.get_all_voyage_at_date(year_int, month_int, day_int)
        available_planes = []
        busy_planes = []
        for voyage in voyages_at_same_date:
            busy_planes.append(voyage.airplane)
        for airplane in airplanes:
            if airplane.name not in busy_planes:
                available_planes.append(airplane)
        return available_planes