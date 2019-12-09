import dateutil.parser

'''Print functions
    
    documented in seperated print_functions.py file to be called in other parts of the system

    print functions are re-used in many parts of the system, for ease of access and change-ability they are
    included in one file.

'''

def header_string(text, length):
    ''' Header string print function

    Args:
        param1(str): text specified
        param2(int): length of print functions, can be changed to suit the length of the text (param1)

    Returns:
        prints chosen string and text string specified

    '''
    string = ("\n" + "*" * length + "\n")
    string += ("*" + " " * (length - 2) + "*" + "\n")
    string += ("*" + text.center((length-2), " ") + "*" + "\n")
    string += ("*" + " " * (length - 2) + "*" + "\n")
    string += ("*" * length + "\n")
    return string

def get_menu():
    print("1: Get employee information")
    print("2: Get destination")
    print("3: Get airplane information")
    print("4: Get voyage schedule")
    print("b: Back")
    print("")

def get_employee_information():
    print("1: All employees")
    print("2: Employee information")
    print("3: Employees by occupation")
    print("4: Employee status")
    print("5: All pilots by airplane model")
    print("6: Pilots by an airplane model")
    print("b: Back")
    print("")

def print_employee_by_occupation():
    print("C for Captain")
    print("P for Pilot")
    print("FA for Flight Attendant")
    print("FSM for Flight Service Manager")
    print("")

def print_employee_by_status():
    print("A for Available")
    print("B for Busy")
    print("")

def print_employee(employees):
    print("{:-<163}".format(""))
    print("{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}{:10}{}".format('| ', 'Occupation *', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Licence', '| ', 'Status **', '|'))
    print("{:-<163}".format(""))
    for item in employees:
        print(item)
    print("{:-<163}".format(""))
    print("* C = Captain, P = Pilot, FA = Flight Attendant, FSM = Flight Service Manager")
    print("** A = Available, B = Busy")
    input("\n**   Press any key to return to main menu    **")

def print_destination(destination):
    print("{:-<128}".format(""))
    print("{}{:25}{}{:25}{}{:10}{}{:10}{}{:30}{}{:15}{}".format('| ', 'Country', '| ',  'Airport', '| ', 'Duration', '| ', 'Distance', '| ', 'Contact name', '| ', 'Contact phone', '|'))
    print("{:-<128}".format(""))
    for item in destination:
        print(item)
    print("{:-<128}".format(""))
    input("\n**   Press any key to return to main menu    **")

def print_airplanes(airplane):
    print("{:-<106}".format(""))
    print("{}{:20}{}{:20}{}{:25}{}{:20}{}{:10}{}".format('| ', 'Name', '| ',  'Model', '| ', 'Producer', '| ', 'Number of seats', '| ', 'Status *', '|'))
    print("{:-<106}".format(""))
    for item in airplane:
        print(item)
    print("{:-<106}".format(""))
    print("* A = Available, I = In the air, LA = Landed abroad")
    input("\n**   Press any key to return to main menu    **")

def print_voyages(voyages):
    print("{:-<94}".format(""))
    print("{}{:20}{}{:20}{}{:25}{}{:20}{}".format('| ', 'Destination', '| ',  'Date', '| ', 'Time', '| ', 'Airplane', '|'))
    print("{:-<94}".format(""))
    for item in voyages:
        print(item)
    print("{:-<94}".format(""))
    input("\n**   Press any key to return to main menu    **")

def print_airport(destination):
    print("{:-<28}".format(""))
    print("{}{:25}{}".format('| ', 'Airport', '|'))
    print("{:-<28}".format(""))
    for item in destination:
        print("{}{:25}{}".format('| ', item.airport, '|'))
    print("{:-<28}".format(""))
    print("")

def print_possible_employee_for_update(employees):
    print("{:-<57}".format(""))
    print("{}{:13}{}{:25}{}{:12}{}".format('| ', 'Occupation *','| ', 'Name', '| ', 'SSN', '|'))
    print("{:-<57}".format(""))
    for item in employees:
        occupation, name, ssn = item.occupation, item.name, item.ssn
        print("{}{:13}{}{:25}{}{:12}{}".format('| ', occupation,'| ', name, '| ', ssn, '|'))
    print("{:-<57}".format(""))
    print("* C = Captain, P = Pilot, FA = Flight Attendant, FSM = Flight Service Manager")
    print("")
    
def print_pilots_by_airplane(pilots):
    print("{:-<163}".format(""))
    print("{}{:10}{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', 'Licence','| ', 'Occupation *', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Status **', '|'))
    print("{:-<163}".format(""))
    pilots = sorted(pilots, key=lambda x: x.licence)
    for item in pilots:
        licence, occupation , name, ssn, address, home_phone, cell_phone, email, licence, emp_status = item.licence, item.occupation , item.name, item.ssn, item.address, item.home_phone, item.cell_phone, item.email, item.licence, item.emp_status
        print("{}{:10}{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', licence,'| ', occupation, '| ', name, '| ', ssn, '| ', address, '| ', home_phone, '| ', cell_phone, '| ', email, '| ', emp_status, '|'))
    print("{:-<163}".format(""))
    print("* C = Captain, P = Pilot")
    input("\n**   Press any key to return to main menu    **")
    print("")

def print_airplane_models(airplanes):
    print("{:-<23}".format(""))
    print("{}{:20}{}".format('| ', 'Model', '|'))
    print("{:-<23}".format(""))
    unique_models = set()
    for item in airplanes:
        unique_models.add(item.model)
    for item in unique_models:
        print("{}{:20}{}".format('| ', item, '|'))
    print("{:-<23}".format(""))
    print("")

def print_airplane_name_and_models(airplanes):
    print("{:-<45}".format(""))
    print("{}{:20}{}{:20}{}".format('| ', 'Name', '| ', 'Model', '|'))
    print("{:-<45}".format(""))
    # unique_models = set()
    airplanes = sorted(airplanes, key=lambda x: x.model)
    for item in airplanes:
        print("{}{:20}{}{:20}{}".format('| ', item.name, '| ', item.model, '|'))
    print("{:-<45}".format(""))
    print("")

def print_pilots_by_model(pilots_model):
    print("{:-<163}".format(""))
    print("{}{:10}{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', 'Licence','| ', 'Occupation *', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Status **', '|'))
    print("{:-<163}".format(""))
    pilots_model = sorted(pilots_model, key=lambda x: x.occupation)
    for item in pilots_model:
        licence, occupation , name, ssn, address, home_phone, cell_phone, email, licence, emp_status = item.licence, item.occupation , item.name, item.ssn, item.address, item.home_phone, item.cell_phone, item.email, item.licence, item.emp_status
        print("{}{:10}{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', licence,'| ', occupation, '| ', name, '| ', ssn, '| ', address, '| ', home_phone, '| ', cell_phone, '| ', email, '| ', emp_status, '|'))
    print("{:-<163}".format(""))
    print("* C = Captain, P = Pilot")
    input("\n**   Press any key to return to continue    **")
    print("")

def print_flight_attendants(flight_attendants):
    print("{:-<153}".format(""))
    print("{}{:10}{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', 'Licence','| ', 'Occupation *', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Status **', '|'))
    print("{:-<153}".format(""))
    flight_attendants = sorted(flight_attendants, key=lambda x: x.occupation)
    for item in flight_attendants:
        occupation , name, ssn, address, home_phone, cell_phone, email, licence, emp_status = item.occupation , item.name, item.ssn, item.address, item.home_phone, item.cell_phone, item.email, item.licence, item.emp_status
        print("{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', occupation, '| ', name, '| ', ssn, '| ', address, '| ', home_phone, '| ', cell_phone, '| ', email, '| ', emp_status, '|'))
    print("{:-<153}".format(""))
    print("* FSM = Flight Service Manager, FA = Flight Attendant")
    print("")

def print_voyages_destination(voyage, airport):
    if voyage == []:
        print("No voyage to " + airport + " on selected date!")
    else:
        print("{:-<67}".format(""))
        print("{}{:20}{}{:25}{}{:15}{}".format('| ', 'Destination', '| ', 'Departure time', '| ', 'Flight number', '|'))
        print("{:-<67}".format(""))
        voyage = sorted(voyage, key=lambda x: x.flight_out)
        for item in voyage:
            destination, departure_date_time, flight_out = item.destination, item.departure, item.flight_out
            print("{}{:20}{}{:25}{}{:15}{}".format('| ', destination, '| ', departure_date_time, '| ', flight_out, '|'))
            print("{:-<67}".format(""))
    print("")

def print_the_voyage(the_voyage_lst):
    the_voyage = the_voyage_lst[0]
    the_destination = the_voyage_lst[1]
    the_captain = the_voyage_lst[2]
    the_pilot = the_voyage_lst[3]
    the_fsm = the_voyage_lst[4]
    the_fa = the_voyage_lst[5]
    print("Information for voyage to " + the_destination.airport + "at " + the_voyage.departure)
    print("")
    print("   Destination: " + the_destination.airport)
    print("   Flight number from Iceland: " + the_voyage.flight_out)
    print("   Departure time from Iceland: " + the_voyage.departure)
    print("   Arrival time at " + the_destination.airport + ": " + the_voyage.arrival_at_dest)
    print("   Flight number to Iceland: " + the_voyage.flight_in)
    print("   Departure time from " + the_destination.airport + ": " + the_voyage.departure_from_dest) #vantar útreikning fyrir þetta
    print("   Arrival time in Iceland: " + the_voyage.arrival_back_home) #vantar útreikning fyrir þetta
    print("   Crew: ")
    if the_captain == 'N/A' and the_pilot == 'N/A' and the_fsm == 'N/A' and the_fa == 'N/A':
        print("      Crew has not been assigned to this voyage!")
    else:
        print("      Captain: " + the_captain.name)
        print("      Pilot: " + the_pilot.name)
        print("      Flight Service Manager: " + the_fsm.name)
        if the_fa == 'N/A':
            print("      No Flight Attendant has been assigned to this voyage!")
        else:
            print("      Flight Attendant: " + the_fa.name)
    print("   Contact person: " + the_destination.contact_name)
    print("   Contact person's phone number: " + the_destination.contact_phone)
    # print("   Total seats on plane for this voyage: " + )
    input("\n**   Press any key to return to main menu    **")
    print("")

def choose_occupation():
    print("** Please choose occupation **")
    print("1: Captain")
    print("2: Pilot")
    print("3: Flight Attendant")
    print("4: Flight Service Manager")
    print("b: Back")
    print("")
