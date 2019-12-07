from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
from models.Voyage import Voyage
import csv

class Get_DL:
    
    def __init__(self):
        self.__destination = []
        self.__employee = []
        self.__airplane = []
        self.__voyage = []

    def get_employee(self):
        employee = []
        if employee == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_employee = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                    employee.append(new_employee)
        return employee

    def get_employee_information(self, employee):
        employee_info_lst = []
        if employee_info_lst == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['ssn'] == employee:
                        employee_info = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        employee_info_lst.append(employee_info)
        return employee_info_lst
    
    def get_employee_by_occupation(self, occupation):
        employee_occupation = []
        if employee_occupation == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['occupation'] == occupation:
                        employee_by_occupation = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        employee_occupation.append(employee_by_occupation)
        return employee_occupation
    
    def get_employee_by_status(self, emp_status):
        employee_status = []
        if employee_status == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['status'] == emp_status:
                        employee_by_status = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        employee_status.append(employee_by_status)
        return employee_status

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

    def get_voyage(self):
        if self.__voyage == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_voyage = Voyage(row['destination'], row['date'], row['time'], row['airplane'])
                    self.__voyage.append(new_voyage)
        return self.__voyage

    def get_pilots_by_airplane(self):
        planes_and_pilots = []
        if planes_and_pilots == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['occupation'] == 'C' or row['occupation'] == 'P':
                        the_planes_and_pilots = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        planes_and_pilots.append(the_planes_and_pilots)
        return planes_and_pilots