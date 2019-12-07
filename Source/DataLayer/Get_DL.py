from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
import csv

class Get_DL:
    
    def __init__(self):
        self.__destination = []
        self.__employee = []
        self.__airplane = []

    def get_employee(self):
        if self.__employee == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_employee = Employee(row['occupation'], row['id'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'])
                    self.__employee.append(new_employee)
        return self.__employee

    def get_destination(self):
        if self.__destination == []:
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], row['contact_phone'])
                    self.__destination.append(new_destination)
        return self.__destination

    def get_airplane(self):
        if self.__airplane == []:
            with open("./data/airplanes.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_airplane = Airplane(row['name'], row['model'], row['producer'], row['number_of_seats'])
                    self.__airplane.append(new_airplane)
        return self.__airplane