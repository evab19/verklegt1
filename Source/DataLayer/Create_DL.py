import csv

class Create_DL:

    def add_employee(self, employee):
        occupation_str = employee.get_occupation()
        # id_str = employee.get_id()
        name_str = employee.get_name()
        ssn_str = employee.get_ssn()
        address_str = employee.get_address()
        home_phone_str = employee.get_home_phone()
        cell_phone_str = employee.get_cell_phone()
        email_str = employee.get_email()
        licence_str = employee.get_licence()
        with open("./data/employee.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['occupation', 'name', 'ssn', 'address', 'home_phone', 'cell_phone', 'email', 'licence']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'occupation': occupation_str, 'name': name_str, 'ssn': ssn_str, 'address': address_str, 'home_phone': home_phone_str, 'cell_phone': cell_phone_str, 'email': email_str, 'licence': licence_str})
        csv_file.close()

    def add_destination(self, destination):
        country = destination.get_country()
        airport = destination.get_airport()
        duration = destination.get_duration()
        distance = destination.get_distance()
        contact_name = destination.get_contact_name()
        contact_phone = destination.get_contact_phone()
        with open("./data/destinations.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['country', 'airport', 'duration', 'distance', 'contact_name', 'contact_phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'country': country, 'airport': airport, 'duration': duration, 'distance': distance, 'contact_name': contact_name, 'contact_phone': contact_phone})
        csv_file.close()

    def add_airplane(self, airplane):
        name = airplane.get_name()
        model = airplane.get_model()
        producer = airplane.get_producer()
        number_of_seats = airplane.get_number_of_seats()
        plane_status = airplane.get_plane_status()
        with open("./data/airplanes.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['name', 'model', 'producer', 'number_of_seats', 'status']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'name': name, 'model': model, 'producer': producer, 'number_of_seats': number_of_seats, 'status': plane_status})
        csv_file.close()

    def add_voyage(self, voyage):
        destination = voyage.get_destination()
        departure = voyage.get_departure()
        airplane = voyage.get_airplane()
        captain = voyage.get_captain()
        pilot = voyage.get_pilot()
        fsm = voyage.get_fsm()
        fa = voyage.get_flight_attendant()
        flight_out = voyage.get_flight_out()
        flight_in = voyage.get_flight_in()
        arrival_at_dest = voyage.get_arrival_at_dest()
        departure_from_dest = voyage.get_departure_from_dest()
        arrival_back_home = voyage.get_arrival_back_home()
        with open("./data/voyage.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['destination', 'departure', 'airplane', 'captain', 'pilot', 'fsm', 'fa', 'flight_out', 'flight_in', 'arrival_at_dest', 'departure_from_dest', 'arrival_back_home']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'destination': destination, 'departure': departure, 'airplane': airplane, 'captain': captain, 'pilot': pilot, 'fsm': fsm, 'fa': fa, 'flight_out': flight_out, 'flight_in': flight_in, 'arrival_at_dest': arrival_at_dest, 'departure_from_dest': departure_from_dest, 'arrival_back_home': arrival_back_home})
        csv_file.close()
 
