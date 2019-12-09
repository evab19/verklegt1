from models.Airplane import Airplane

class AirplaneLL:
    '''Logic Layer Airplane Class

        Logic layer classes receive information from the LLAPI class for processing.
        Information is passed on to IOAPI which interacts with data layer classes

    '''

    def __init__(self, dapi_in):
        self.__airplane_repo = dapi_in 
        self.__airplane = Airplane()

    def add_airplane(self, __airplane):
        if self.is_valid_airplane(__airplane):
            self.__airplane_repo.add_airplane(__airplane)
     
    def is_valid_airplane(self, __airplane):
        #here should be some code to 
        #validate the video
        return True
 
    def get_airplane(self):
        return self.__airplane_repo.get_airplane()