from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
from models.Voyage import Voyage
import csv

class DataAPI:
    
    def __init__(self):
        self.__destinations = []
        self.__employee = []
        self.__airplane = []
        self.__voyage = []

    def add_employee(self, employee):
        occupation_str = employee.get_occupation()
        id_str = employee.get_id()
        name_str = employee.get_name()
        ssn_str = employee.get_ssn()
        address_str = employee.get_address()
        home_phone_str = employee.get_home_phone()
        cell_phone_str = employee.get_cell_phone()
        email_str = employee.get_email()
        licence_str = employee.get_licence()
        with open("./data/employee.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['occupation', 'id', 'name', 'ssn', 'address', 'home_phone', 'cell_phone', 'email', 'licence']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'occupation': occupation_str, 'id': id_str, 'name': name_str, 'ssn': ssn_str, 'address': address_str, 'home_phone': home_phone_str, 'cell_phone': cell_phone_str, 'email': email_str, 'licence': licence_str})
        csv_file.close()

    def get_employee(self):
        if self.__employee == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_employee = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'])
                    self.__employee.append(new_employee)
        return self.__employee


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
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], row['contact_phone'])
                    self.__destinations.append(new_destination)
        return self.__destinations

 
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
            with open("./data/airplanes.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_airplane = Airplane(row['name'], row['model'], row['producer'], row['number_of_seats'])
                    self.__airplane.append(new_airplane)
        return self.__airplane

    def add_voyage(self, voyage):
        destination = voyage.get_destination()
        date = voyage.get_date()
        time = voyage.get_time()
        airplane = voyage.get_airplane()
        with open("./data/voyage.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['destination', 'date', 'time', 'airplane']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'destination': destination, 'date': date, 'time': time, 'airplane': airplane})
        csv_file.close()
 
    def get_voyage(self):
        if self.__voyage == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_voyage = Voyage(row['destination'], row['date'], row['time'], row['airplane'])
                    self.__voyage.append(new_voyage)
        return self.__voyage