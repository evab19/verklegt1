from models.Airplane import Airplane

class AirplaneLL:

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, airplane):
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
     
    def is_valid_airplane(self, airplane):
        #here should be some code to 
        #validate the video
        return True
 
    def get_airplane(self):
        return self.__airplane_repo.get_airplane()