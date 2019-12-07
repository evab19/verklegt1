def header_string(text, length):
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
    print("5: Pilots by airplane type")
    print("b: Back")
    print("")

def print_employee(employees):
    print("{:-<151}".format(""))
    print("{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}{:10}{}".format('| ', 'Occupation', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Licence', '| ', 'Status **' '|'))

def print_employee_by_occupation():
    print("C for Captain")
    print("P for Pilot")
    print("FA for Flig Attendant")
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
    print("{:-<94}".format(""))
    print("{}{:20}{}{:20}{}{:25}{}{:20}{}".format('| ', 'Name', '| ',  'Model', '| ', 'Producer', '| ', 'Number of seats', '|'))
    print("{:-<94}".format(""))
    for item in airplane:
        print(item)
    print("{:-<94}".format(""))
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
    print("{}{:25}{}".format('| ',  'Airport', '|'))
    print("{:-<28}".format(""))
    for item in destination:
        print(item.airport)
    print("{:-<28}".format(""))

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
