from DataLayer.DataAPI import DataAPI

class DestinationAPI:
    def __init__(self):
        self.__destination_repo = DataAPI()
        self.__airplane_repo = DataAPI()

    def add_destination(self, destination):
        if self.is_valid_destination(destination):
            self.__destination_repo.add_destination(destination)
    
    def is_valid_destination(self, destination):
        #here should be some code to 
        #validate the video
        return True

    def get_destinations(self):
        return self.__destination_repo.get_destinations()

    def get_destinations_by_country(self, country):
        pass

    ###airplane update
    def add_airplane(self, airplane):
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
    
    def is_valid_airplane(self, airplane):
        #here should be some code to 
        #validate the video
        return True

    def get_airplane(self):
        return self.__airplane_repo.get_airplane()
