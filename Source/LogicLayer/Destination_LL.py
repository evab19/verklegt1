from models.Destination import Destination

class DestinationLL:

    def __init__(self, dapi_in):
        self.__destination_repo = dapi_in 
        self.__destination = Destination()

    def add_destination(self, __destination):
        if self.is_valid_destination(__destination):
            self.__destination_repo.add_destination(__destination)
    
    def is_valid_destination(self, __destination):
        #here should be some code to 
        #validate the video
        return True

    def get_destination(self):
        return self.__destination_repo.get_destination()

    def get_destinations_by_country(self, country):
        pass

    def update_destination(self, destination, new_contact):
        self.__destination_repo.update_destination(destination, new_contact)