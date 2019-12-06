from models.Destination import Destination
from models.Airplane import Airplane
import csv

class DataAPI:
    
    def __init__(self):
        self.__destinations = []
        self.__employee = []
        self.__airplane = []

    def add_employee(self, employee):
        # first add to file then to private list
        occupation_str = employee.get_occupation()
        id_str = employee.get_id()
        name_str = employee.get_name()
        so_str = employee.get_so()
        address_str = employee.get_address()
        home_phone_str = employee.get_home_phone()
        cell_phone_str = employee.get_cell_phone()
        email_str = employee.get_email()
        licence_str = employee.get_licence()
        with open("./data/employee.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['occupation_str', 'id_str', 'name_str', 'so_str', 'address_str', 'home_phone_str', 'cell_phone_str', 'email_str', 'licence_str']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'occupation_str': occupation_str, 'id_str': id_str, 'name_str': name_str, 'so_str': so_str, 'address_str': address_str, 'home_phone_str': home_phone_str, 'cell_phone_str': cell_phone_str, 'email_str': email_str, 'licence_str': licence_str})
        csv_file.close()

    def get_employee(self):
        if self.__employee == []:
            employee_str = ""
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:

                    print(row['occupation_str'] + ', ' + row['id_str'] + ', ' + row['name_str'] + ', ' + row['so_str'] + ', ' + row['address_str'] + ', ' + row['home_phone_str'] + ', ' + row['cell_phone_str'] + ', ' + row['email_str'] + ', ' + row['licence_str'])

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
 
    def get_destinations(self):
        if self.__destinations == []:
            destination_str = ""
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['country'] + ', ' + row['airport'] + ', ' + row['duration'] + ', ' + row['distance'] + ', ' + row['contact_name'] + ', ' + row['contact_phone'])
                 
 
    def add_airplane(self, airplane):
        name = airplane.get_name()
        model = airplane.get_model()
        producer = airplane.get_producer()
        number_of_seats = airplane.get_number_of_seats()
        with open("./data/airplanes.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['name', 'model', 'producer', 'number_of_seats']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'name': name, 'model': model, 'producer': producer, 'number_of_seats': number_of_seats})
        csv_file.close()
 
    def get_airplane(self):
        if self.__airplane == []:
            airplane_str = ""
            with open("./data/airplanes.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['name'] + ', ' + row['model'] + ', ' + row['producer'] + ', ' + row['number_of_seats'])