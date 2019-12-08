class Voyage():
    
    def __init__(self, destination = "", departure = "", airplane = "", captain = "N/A", pilot = "N/A", fsm = "N/A", fa = "N/A", flight_out = "N/A", flight_in = "N/A"):
        self.destination = destination
        self.departure = departure
        self.captain = captain
        self.pilot = pilot
        self.flight_attendant = fa
        self.fsm = fsm
        self.airplane = airplane
        self.flight_out = flight_out
        self.flight_in = flight_in
        self.arrival_at_dest = ""
        self.departure_from_dest = ""
        self.arrival_back_home = ""

    def get_destination(self):
        return self.destination
    
    def get_departure(self):
        return self.departure
    
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
    
    def get_flight_out(self):
        return self.flight_out

    def get_flight_in(self):
        return self.flight_in

    def get_arrival_at_dest(self):
        return self.arrival_at_dest

    # def __str__(self):
    #     return "{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', self.destination, '| ', self.departure, '| ', self.airplane, '|', self.captain, '| ', self.pilot, '| ', self.fsm, '| ', self.flight_attendant, '| ')



    

