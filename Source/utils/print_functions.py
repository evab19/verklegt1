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
    print("5: Pilots by licence")
    print("6: Pilots by airplane type")
    print("b: Back")
    print("")

<<<<<<< Updated upstream
def get_employee_by_occupation():
=======
def print_employee(employees):
    print("{:-<151}".format(""))
    print("{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}{:10}{}".format('| ', 'Occupation', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Licence', '| ', 'Status **' '|'))

def print_employee_by_occupation():
>>>>>>> Stashed changes
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