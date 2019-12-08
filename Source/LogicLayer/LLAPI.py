from LogicLayer.Destination_LL import DestinationLL
from LogicLayer.Employee_LL import EmployeeLL
from LogicLayer.Airplane_LL import AirplaneLL
from LogicLayer.Voyage_LL import VoyageLL
from DataLayer.DataAPI import DataAPI


class LLAPI:
    def __init__(self):
        self.__dapi = DataAPI()
        self.__employee = EmployeeLL(self.__dapi)
        self.__airplane = AirplaneLL(self.__dapi)
        self.__destination = DestinationLL(self.__dapi)
        self.__voyage = VoyageLL(self.__dapi)

#### destination
    def add_destination(self, __destination):
        if self.__destination.is_valid_destination(__destination):
            self.__destination.add_destination(__destination)

    def get_destination(self):
         return self.__destination.get_destination()

    def update_destination(self, destination, new_contact):
        self.__destination.update_destination(destination, new_contact)
    
#### employee
    def add_employee(self, __employee):
        if self.__employee.is_valid_employee(__employee):
            self.__employee.add_employee(__employee)
    
    def get_employee(self):
        return self.__employee.get_employee()

    def update_employee(self, employee, new_employee):
        self.__employee.update_employee(employee, new_employee)
    
    def get_employee_information(self, __employee):
        return self.__employee.get_employee_information(__employee)

    def get_employee_by_occupation(self, __occupation):
        return self.__employee.get_employee_by_occupation(__occupation)
    
    def get_employee_by_status(self, __emp_status):
        return self.__employee.get_employee_by_status(__emp_status)
        
    def get_pilots_by_airplane(self):
        return self.__employee.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        return self.__employee.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        return self.__employee.get_flight_attendants()

#### airplane
    def add_airplane(self, __airplane):
        if self.__airplane.is_valid_airplane(__airplane):
            self.__airplane.add_airplane(__airplane)
 
    def get_airplane(self):
        return self.__airplane.get_airplane()

#### voyage
    def add_voyage(self, __voyage):
        #if self.is_valid_voyage(__voyage):
        self.__voyage.add_voyage(__voyage)
 
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        return self.__voyage.get_voyage_destination(voyage_destination, year_int, month_int, day_int)
    
    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        return self.__voyage.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)