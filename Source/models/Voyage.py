class Voyage():
    
    def __init__(self, destination = "", date = "", time = "", airplane = "", pilot = "", flight_attendant = "", fsm = "", captain = ""):
        self.destination = destination
        self.date = date
        self.time = time
        self.captain = captain
        self.pilot = pilot
        self.flight_attendant = flight_attendant
        self.fsm = fsm
        self.airplane = airplane

    def get_destination(self):
        return self.destination
    
    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time
    
    def get_captain(self):
        return self.captain

    def get_pilot(self):
        return self.pilot

    def get_flight_attendant(self):
        return self.flight_attendant

    def get_fsm(self):
        return self.fsm

    def get_airplane(self):
        return self.airplane

    
    def __str__(self):
        return "{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', self.destination, '| ', self.date, '| ', self.time, '| ', self.airplane, '|', self.captain, '| ', self.pilot, '| ', self.fsm, '| ', self.flight_attendant, '| ')



    

