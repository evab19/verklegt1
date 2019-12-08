from models.Airplane import Airplane

class AirplaneLL:

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, __airplane):
        if self.is_valid_airplane(__airplane):
            self.__airplane_repo.add_airplane(__airplane)
     
    def is_valid_airplane(self, __airplane):
        if __airplane.name and __airplane.model and __airplane.producer and __airplane.number_of_seats and __airplane.status != "":
            return True
        else:
            return False
 
    def get_airplane(self):
        return self.__airplane_repo.get_airplane()