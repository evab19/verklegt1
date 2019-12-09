from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
from models.Voyage import Voyage
import csv
# from dateutil import parser
import dateutil.parser

class Get_DL:
    
    def __init__(self):
        self.__destination = []
        self.__employee = []
        self.__airplane = []
        self.__voyage = []

    def get_employee(self):
        employee_lst = []
        if employee_lst == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_employee = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                    employee_lst.append(new_employee)
        return employee_lst

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
        employee_occupation_lst = []
        if employee_occupation_lst == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['occupation'] == occupation:
                        employee_by_occupation = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        employee_occupation_lst.append(employee_by_occupation)
        return employee_occupation_lst
    
    def get_employee_by_status(self, emp_status):
        employee_status_lst = []
        if employee_status_lst == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['status'] == emp_status:
                        employee_by_status = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        employee_status_lst.append(employee_by_status)
        return employee_status_lst

    def get_destination(self):
        destination_lst = []
        if destination_lst == []:
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], row['contact_phone'])
                    destination_lst.append(new_destination)
        return destination_lst

    def get_airplane(self):
        airplane_lst = []
        if airplane_lst == []:
            with open("./data/airplanes.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_airplane = Airplane(row['name'], row['model'], row['producer'], row['number_of_seats'], row['status'])
                    airplane_lst.append(new_airplane)
        return airplane_lst

    def get_voyage(self):
        voyage_lst = []
        if voyage_lst == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_voyage = Voyage(row['destination'], row['date'], row['time'], row['airplane'])
                    voyage_lst.append(new_voyage)
        return voyage_lst

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

    def get_pilots_by_model(self, pilots_model):
        models_and_pilots = []
        if models_and_pilots == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['licence'] == pilots_model:
                        the_models_and_pilots = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        models_and_pilots.append(the_models_and_pilots)
        return models_and_pilots

    def get_flight_attendants(self):
        flight_attendants = []
        if flight_attendants == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['occupation'] == 'FA' or row['occupation'] == 'FSM':
                        the_flight_attendants = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                        flight_attendants.append(the_flight_attendants)
        return flight_attendants

    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        voyage_destination_lst = []
        if voyage_destination_lst == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['destination'] == voyage_destination:
                        voyage_departure = dateutil.parser.parse(row['departure_date_time'])
                        voyage_year = voyage_departure.year
                        voyage_month = voyage_departure.month
                        voyage_day = voyage_departure.day
                        if voyage_year == year_int and voyage_month == month_int and voyage_day == day_int:
                            the_voyage_destination = Voyage(row['destination'], row['departure_date_time'], row['airplane_name'], row['captain_ssn'], row['pilot_ssn'], row['fsm_ssn'], row['fa_ssn'], row['flight_out'], row['flight_in'])
                            voyage_destination_lst.append(the_voyage_destination)
        return voyage_destination_lst

    def get_destination_by_airport_class(self, airport):
        with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['airport'].lower() == airport.lower():
                    new_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], row['contact_phone'])
                    return new_destination
    
    def get_employee_information_class(self, employee):
        with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['ssn'] == employee:
                    employee_info = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'], row['status'])
                    return employee_info

    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        voyage_lst_inst = []
        if voyage_lst_inst == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['destination'] == voyage_destination:
                        voyage_departure = dateutil.parser.parse(row['departure_date_time'])
                        voyage_year = voyage_departure.year
                        voyage_month = voyage_departure.month
                        voyage_day = voyage_departure.day
                        if voyage_year == year_int and voyage_month == month_int and voyage_day == day_int and row['flight_out'] == flight_number:
                            the_voyage = Voyage(row['destination'], row['departure_date_time'], row['airplane_name'], row['captain_ssn'], row['pilot_ssn'], row['fsm_ssn'], row['fa_ssn'], row['flight_out'], row['flight_in'], row['arrival_at_dest'], row['departure_from_dest'], row['arrival_back_home'])
                            voyage_lst_inst.append(the_voyage)
                            the_airport = row['destination']
                            the_destination = self.get_destination_by_airport_class(the_airport)
                            voyage_lst_inst.append(the_destination)
                            if row['captain_ssn'] == 'N/A':
                                voyage_lst_inst.append('N/A')
                            else:
                                the_captain = self.get_employee_information_class(row['captain_ssn'])
                                voyage_lst_inst.append(the_captain)
                            if row['pilot_ssn'] == 'N/A':
                                voyage_lst_inst.append('N/A')
                            else:
                                the_pilot = self.get_employee_information_class(row['pilot_ssn'])
                                voyage_lst_inst.append(the_pilot)
                            if row['fsm_ssn'] == 'N/A':
                                voyage_lst_inst.append('N/A')
                            else:
                                the_fsm = self.get_employee_information_class(row['fsm_ssn'])
                                voyage_lst_inst.append(the_fsm)
                            if row['fa_ssn'] == 'N/A':
                                voyage_lst_inst.append('N/A')
                            else:
                                the_fa = self.get_employee_information_class(row['fa_ssn'])
                                voyage_lst_inst.append(the_fa)
        return voyage_lst_inst
    

    def get_all_voyage_at_date(self, year_int, month_int, day_int):
        voyage_destination_lst = []
        if voyage_destination_lst == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    voyage_departure = dateutil.parser.parse(row['departure_date_time'])
                    voyage_year = voyage_departure.year
                    voyage_month = voyage_departure.month
                    voyage_day = voyage_departure.day
                    if voyage_year == year_int and voyage_month == month_int and voyage_day == day_int:
                        the_voyage_by_date = Voyage(row['destination'], row['departure_date_time'], row['airplane_name'], row['captain_ssn'], row['pilot_ssn'], row['fsm_ssn'], row['fa_ssn'], row['flight_out'], row['flight_in'])
                        voyage_destination_lst.append(the_voyage_by_date)
        return voyage_destination_lst
