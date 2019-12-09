from models.Airplane import Airplane

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
        return self.__airplane_repo.get_airplane()

    def get_airplane_status(self, year_int, month_int, day_int):
        airplanes = self.__airplane_repo.get_airplane()
        other_voyages = self.__airplane_repo.get_all_voyage_at_date(year_int, month_int, day_int)
        available_planes = []
        busy_planes = []
        for voyage in other_voyages:
            busy_planes.append(voyage.airplane)
        for airplane in airplanes:
            if airplane.name not in busy_planes:
                available_planes.append(airplane)
        return available_planes