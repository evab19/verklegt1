from models.Voyage import Voyage

class VoyageLL:

    def __init__(self, dapi_in):
        self.__voyage_repo = dapi_in 
        self.__voyage = Voyage()

    def add_voyage(self, __voyage):
        if self.is_valid_voyage(__voyage):
            self.__voyage_repo.add_voyage(__voyage)

    def is_valid_voyage(self, __voyage):
        #add code here to verify
        return True
    
    def get_voyage(self):
        return self.__voyage_repo.get_voyage()