class Airplane:
 
    def __init__(self, name = "", model = "", producer = "", number_of_seats = ""):
        self.name = name
        self.model = model
        self.producer = producer
        self.number_of_seats = number_of_seats
    
    def __str__(self):
        return "{}{:20}{}{:20}{}{:25}{}{:20}{}".format('| ', self.name, '| ', self.model, '| ', self.producer, '| ', self.number_of_seats, '|')
 
    def get_name(self):
        return str(self.name)
     
    def get_model(self):
        return str(self.model)
     
    def get_producer(self):
        return str(self.producer)
     
    def get_number_of_seats(self):
        return str(self.number_of_seats)