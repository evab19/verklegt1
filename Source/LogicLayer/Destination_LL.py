from models.Destination import Destination

class DestinationLL:
      '''Logic Layer Destination Class

        Logic layer classes receive information from the LLAPI class for processing.
        Information is passed on to IOAPI which interacts with data layer classes
    '''

    def __init__(self, dapi_in):
        self.__destination_repo = dapi_in 
        self.__destination = Destination()

    def add_destination(self, destination):
        if self.is_valid_destination(destination):
            self.__destination_repo.add_destination(destination)
            return True
        else:
            return False
    
    def is_valid_destination(self, destination):
        #self, country = "", airport = "", duration = "", distance = "", contact_name = "", contact_phone = ""):
        if destination.country and destination.airport and destination.duration and destination.distance and destination.contact_name and destination.contact_phone != "":
            return True
        else:
            return False

    def get_destination(self):
        return self.__destination_repo.get_destination()

    def get_destinations_by_country(self, country):
        pass

    def update_destination(self, destination, new_contact):
        self.__destination_repo.update_destination(destination, new_contact)