from DataLayer.Get_DL import Get_DL
from DataLayer.Create_DL import Create_DL
from DataLayer.Update_DL import Update_DL
import csv


class DataAPI:
    '''Data Layer API
       --------------

        DataApi receives data from the logic layer which is either sent 
        for storage to data tables or uses IDs received from logic layer to 
        collect data from data layer and returns this back up.

        Param:
        ------
        get: 
        create:
        update:
        
    '''

    def __init__(self):
        self.__get = Get_DL()
        self.__create = Create_DL()
        self.__update = Update_DL()

# add/create föll
    def add_employee(self, employee):
        return self.__create.add_employee(employee)

    def add_destination(self, destination):
        return self.__create.add_destination(destination)

    def add_airplane(self, airplane):
        return self.__create.add_airplane(airplane)

    def add_voyage(self, voyage):
        return self.__create.add_voyage(voyage)
    
    def check_if_ssn_unique(self, ssn):
        employees = self.get_employee()
        return not(any(employee.ssn == ssn for employee in employees))

# get föll
    def get_employee(self):
        return self.__get.get_employee()
    
    def get_employee_information(self, employee):
        return self.__get.get_employee_information(employee)

    def get_employee_by_occupation(self, occupation):
        return self.__get.get_employee_by_occupation(occupation)
    def get_employee_by_status(self, emp_status):
        return self.__get.get_employee_by_status(emp_status)

    def get_pilots_by_airplane(self):
        return self.__get.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        return self.__get.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        return self.__get.get_flight_attendants()

    def get_destination(self):
        return self.__get.get_destination()

    def get_airplane(self):
        return self.__get.get_airplane()

    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        return self.__get.get_voyage_destination(voyage_destination, year_int, month_int, day_int)
    
    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        return self.__get.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)

    def get_all_voyage_at_date(self, year_int, month_int, day_int):
        return self.__get.get_all_voyage_at_date(year_int, month_int, day_int)

    def get_destination_by_airport_class(self, airport):
        return self.__get.get_destination_by_airport_class(airport)

# update föll
    def update_destination(self, destination, new_contact):
        return self.__update.update_destination(destination, new_contact)

    def update_employee(self, employee, new_employee):
        self.__update.update_employee(employee, new_employee)
    
    def update_voyage(self, the_voyage, captain_str, pilot_str, fsm_str, fa_str):
        self.__update.update_voyage(the_voyage, captain_str, pilot_str, fsm_str, fa_str)