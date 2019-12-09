class Airplane:
    '''Module Airplane class

        Module classes are used by the logic layer classes to create new instances of Airplane
    
        
        gets an instance of a Airplane information list

        returns:
            name
            model
            producer
            number_of_seats
            plane_status
    '''
    
 
    def __init__(self, name = "", model = "", producer = "", number_of_seats = "", plane_status = "A"):
        self.name = name
        self.model = model
        self.producer = producer
        self.number_of_seats = number_of_seats
        self.plane_status = plane_status
    
    def __str__(self):
        return "{}{:20}{}{:20}{}{:25}{}{:20}{}{:10}{}".format('| ', self.name, '| ', self.model, '| ', self.producer, '| ', str(self.number_of_seats), '| ', str(self.plane_status), '|')
 
    def get_name(self):
        return str(self.name)
     
    def get_model(self):
        return str(self.model)
     
    def get_producer(self):
        return str(self.producer)
     
    def get_number_of_seats(self):
        return str(self.number_of_seats)
    
    def get_plane_status(self):
        return str(self.plane_status)