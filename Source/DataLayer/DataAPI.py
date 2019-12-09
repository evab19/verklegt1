from DataLayer.Get_DL import Get_DL
from DataLayer.Create_DL import Create_DL
from DataLayer.Update_DL import Update_DL
import csv


class DataAPI:

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

# get föll

    def get_destination(self):
        return self.__get.get_destination()

    def get_airplane(self):
        return self.__get.get_airplane()

    def get_voyage(self):
        return self.__get.get_voyage()

# update föll
    def update_destination(self, destination, new_contact):
        return self.__update.update_destination(destination, new_contact)

    def update_employee(self, employee, new_employee):
        self.__update.update_employee(employee, new_employee)