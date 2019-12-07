from DataLayer.Get_DL import Get_DL
from DataLayer.Create_DL import Create_DL
import csv


class DataAPI:

    def __init__(self):
        self.__get = Get_DL()
        self.__create = Create_DL()

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

    def get_destination(self):
        return self.__get.get_destination()

    def get_airplane(self):
        return self.__get.get_airplane()

    def get_voyage(self):
        return self.__get.get_voyage()
