from LogicLayer.Destination_LL import DestinationLL
from LogicLayer.Employee_LL import EmployeeLL
from LogicLayer.Airplane_LL import AirplaneLL
from DataLayer.DataAPI import DataAPI


class LLAPI:
    def __init__(self):
        self.__dapi = DataAPI()
        self.__employee = EmployeeLL(self.__dapi)
        self.__airplane = AirplaneLL(self.__dapi)
        self.__destination = DestinationLL(self.__dapi)

#### destination
    def add_destination(self, __destination):
       # if self.is_valid_destination(__destination):
            self.__destination.add_destination(__destination)

    def get_destinations(self):
         return self.__destination.get_destinations()
    

#### employee
    def add_employee(self, __employee):
        #if self.is_valid_employee(__employee):
            self.__employee.add_employee(__employee)
    
    def get_employee(self):
        return self.__employee.get_employee()

#### airplane
    def add_airplane(self, __airplane):
       # if self.is_valid_airplane(__airplane):
            self.__airplane.add_airplane(__airplane)
 
    def get_airplane(self):
        return self.__airplane.get_airplane()