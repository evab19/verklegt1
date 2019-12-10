import dateutil.parser

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
    print("5: All pilots by airplane model")
    print("6: Pilots by an airplane model")
    print("7: Employee week schedule")
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
    input("\n**   Press any key to continue    **")
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
    print("   Departure time from " + the_destination.airport + ": " + the_voyage.departure_from_dest)
    print("   Arrival time in Iceland: " + the_voyage.arrival_back_home)
    print("")
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
    input("\n**   Press any key to return to main menu    **")
    print("")

def print_employee_schedule(employee, week_lst, schedule_lst):
    length = 17
    times = 7
    length_header = length * 3
    employee_name = employee[0].name
    start_date = str(week_lst[0])
    start_date_print = str(start_date[:4]) + "-" + str(start_date[4:6]) + "-" + str(start_date[6:])
    end_date = str(week_lst[6])
    end_date_print = str(end_date[:4]) + "-" + str(end_date[4:6]) + "-" + str(end_date[6:])

    def check_hour_min(check_num1, check_num2):
        if check_num1 < 10:
            check_num1 = "0" + str(check_num1)
        if check_num2 < 10:
            check_num2 = "0" + str(check_num2)
        return check_num1, check_num2
    
    def parse_hour_min(temp_dep_time, temp_arr_time):
        dep_time = dateutil.parser.parse(temp_dep_time)
        dep_hour, dep_min = dep_time.hour, dep_time.minute
        dep_hour, dep_min = check_hour_min(dep_hour, dep_min)
        
        arr_time = dateutil.parser.parse(temp_arr_time)
        arr_hour, arr_min = arr_time.hour, arr_time.minute
        arr_hour, arr_min = check_hour_min(arr_hour, arr_min)
        
        return dep_hour, dep_min, arr_hour, arr_min

    if schedule_lst[0] == "N/A":
        mon_destination, mon_departure, mon_arrival = "DAY OFF", "---", "---"
    else:
        mon_dep_hour, mon_dep_min, mon_arr_hour, mon_arr_min = parse_hour_min(schedule_lst[0].departure, schedule_lst[0].arrival_back_home)
        mon_destination, mon_departure, mon_arrival = schedule_lst[0].destination, str(mon_dep_hour) + ":" + str(mon_dep_min), str(mon_arr_hour) + ":" + str(mon_arr_min)
    if schedule_lst[1] == "N/A":
        tue_destination, tue_departure, tue_arrival = "DAY OFF", "---", "---"
    else:
        tue_dep_hour, tue_dep_min, tue_arr_hour, tue_arr_min = parse_hour_min(schedule_lst[1].departure, schedule_lst[1].arrival_back_home)
        tue_destination, tue_departure, tue_arrival = schedule_lst[1].destination, str(tue_dep_hour) + ":" + str(tue_dep_min), str(tue_arr_hour) + ":" + str(tue_arr_min)
    if schedule_lst[2] == "N/A":
        wed_destination, wed_departure, wed_arrival = "DAY OFF", "---", "---"
    else:
        wed_dep_hour, wed_dep_min, wed_arr_hour, wed_arr_min = parse_hour_min(schedule_lst[2].departure, schedule_lst[2].arrival_back_home)
        wed_destination, wed_departure, wed_arrival = schedule_lst[2].destination, str(wed_dep_hour) + ":" + str(wed_dep_min), str(wed_arr_hour) + ":" + str(wed_arr_min)
    if schedule_lst[3] == "N/A":
        thu_destination, thu_departure, thu_arrival = "DAY OFF", "---", "---"
    else:
        thu_dep_hour, thu_dep_min, thu_arr_hour, thu_arr_min = parse_hour_min(schedule_lst[3].departure, schedule_lst[3].arrival_back_home)
        thu_destination, thu_departure, thu_arrival = schedule_lst[3].destination, str(thu_dep_hour) + ":" + str(thu_dep_min), str(thu_arr_hour) + ":" + str(thu_arr_min)
    if schedule_lst[4] == "N/A":
        fri_destination, fri_departure, fri_arrival = "DAY OFF", "---", "---"
    else:
        fri_dep_hour, fri_dep_min, fri_arr_hour, fri_arr_min = parse_hour_min(schedule_lst[4].departure, schedule_lst[4].arrival_back_home)
        fri_destination, fri_departure, fri_arrival = schedule_lst[4].destination, str(fri_dep_hour) + ":" + str(fri_dep_min), str(fri_arr_hour) + ":" + str(fri_arr_min)
    if schedule_lst[5] == "N/A":
        sat_destination, sat_departure, sat_arrival = "DAY OFF", "---", "---"
    else:
        sat_dep_hour, sat_dep_min, sat_arr_hour, sat_arr_min = parse_hour_min(schedule_lst[5].departure, schedule_lst[5].arrival_back_home)
        sat_destination, sat_departure, sat_arrival = schedule_lst[5].destination, str(sat_dep_hour) + ":" + str(sat_dep_min), str(sat_arr_hour) + ":" + str(sat_arr_min)
    if schedule_lst[6] == "N/A":
        sun_destination, sun_departure, sun_arrival = "DAY OFF", "---", "---"
    else:
        sun_dep_hour, sun_dep_min, sun_arr_hour, sun_arr_min = parse_hour_min(schedule_lst[6].departure, schedule_lst[6].arrival_back_home)
        sun_destination, sun_departure, sun_arrival = schedule_lst[6].destination, str(sun_dep_hour) + ":" + str(sun_dep_min), str(sun_arr_hour) + ":" + str(sun_arr_min)

    day_1, day_2, day_3, day_4, day_5, day_6, day_7 = "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
    
    temp_schedule_str = " Schedule for " + employee_name
    temp_date_str = " For the week of " + start_date_print + " to " + end_date_print
    schedule_str = "\n" + "-" * (length_header + 4) + "\n"
    schedule_str += "|" + (" " * (length_header + 2)) + "|\n"
    schedule_str += "|" + temp_schedule_str + (" " * ((length_header + 2) - len(temp_schedule_str))) + "|\n"
    schedule_str += "|" + temp_date_str + (" " * ((length_header + 2) - len(temp_date_str))) + "|\n"
    schedule_str += "|" + (" " * (length_header + 2)) + "|\n"
    schedule_str += "-" * ((length * times) + 8) + "\n"
    schedule_str += (("|" + " " * length) * times) + "|\n"
    schedule_str += ("|" + day_1.center((length), " ") + "|" + day_2.center((length), " ") + "|" + day_3.center((length), " ") + "|" + day_4.center((length), " ") + "|" + day_5.center((length), " ") + "|" + day_6.center((length), " ") + "|" + day_7.center((length), " ") + "|\n")
    schedule_str += (("|" + " " * length) * times) + "|\n"
    schedule_str += "-" * ((length * times) + 8) + "\n"
    schedule_str += (("|" + " " * length) * times) + "|\n"
    schedule_str += (("|" + "Destination:".center(length)) * times + "|\n")
    schedule_str += ("|" + mon_destination.center(length) + "|" + tue_destination.center(length) + "|" + wed_destination.center(length) + "|" + thu_destination.center(length) + "|" + fri_destination.center(length) + "|" + sat_destination.center(length) + "|" + sun_destination.center(length) + "|\n")
    schedule_str += (("|" + " " * length) * times + '|\n')
    schedule_str += (("|" + "Departure".center(length)) * times + "|\n")
    schedule_str += (("|" + "from Iceland:".center(length)) * times + "|\n")
    schedule_str += ("|" + mon_departure.center(length) + "|" + tue_departure.center(length) + "|" + wed_departure.center(length) + "|" + thu_departure.center(length) + "|" + fri_departure.center(length) + "|" + sat_departure.center(length) + "|" + sun_departure.center(length) + "|\n")
    schedule_str += (("|" + " " * length) * times + '|\n')
    schedule_str += (("|" + "Arrival".center(length)) * times + "|\n")
    schedule_str += (("|" + "in Iceland:".center(length)) * times + "|\n")
    schedule_str += ("|" + mon_arrival.center(length) + "|" + tue_arrival.center(length) + "|" + wed_arrival.center(length) + "|" + thu_arrival.center(length) + "|" + fri_arrival.center(length) + "|" + sat_arrival.center(length) + "|" + sun_arrival.center(length) + "|\n")
    schedule_str += (("|" + " " * length) * times + '|\n')
    schedule_str += ("{:-<127}".format(""))
    print(schedule_str)
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
