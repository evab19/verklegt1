from models.Airplane import Airplane

class AirplaneLL:

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, __airplane):
        if self.is_valid_airplane(__airplane):
            self.__airplane_repo.add_airplane(__airplane)
     
    def is_valid_airplane(self, airplane):
        #here should be some code to 
        #validate the video
        return True
 
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