class Voyage():
    '''Module Voyage class

        Module classes are used by the logic layer classes to create new instances of voyage
    
        
        Returns an instance of a voyage information list
        ---------------------------------------------
   

            destination
            departure
            captain
            pilot
            fa
            fsm
            airplane
            flight_out
            flight_in
            arrival_at_dest
            departure_from_dest
            arrival_back_home

    '''
    
    def __init__(self, destination = "", departure = "", airplane = "", captain = "N/A", pilot = "N/A", fsm = "N/A", fa = "N/A", flight_out = "N/A", flight_in = "N/A", arrival_at_dest = "", departure_from_dest = "", arrival_back_home = ""):
        self.destination = destination
        self.departure = departure
        self.captain = captain
        self.pilot = pilot
        self.flight_attendant = fa
        self.fsm = fsm
        self.airplane = airplane
        self.flight_out = flight_out
        self.flight_in = flight_in
        self.arrival_at_dest = arrival_at_dest
        self.departure_from_dest = departure_from_dest
        self.arrival_back_home = arrival_back_home

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
    
    def get_departure_from_dest(self):
        return self.departure_from_dest

    def get_arrival_back_home(self):
        return self.arrival_back_home

    # def __str__(self):
    #     return "{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', self.destination, '| ', self.departure, '| ', self.airplane, '|', self.captain, '| ', self.pilot, '| ', self.fsm, '| ', self.flight_attendant, '| ')



    

