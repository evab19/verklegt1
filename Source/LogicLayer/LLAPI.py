from LogicLayer.Destination_LL import DestinationLL
from LogicLayer.Employee_LL import EmployeeLL
from LogicLayer.Airplane_LL import AirplaneLL
from LogicLayer.Voyage_LL import VoyageLL
from DataLayer.DataAPI import DataAPI


class LLAPI:
    '''LLAPI data receiver and transmitter

        LLAPI receives information input by user in the UI layer and sends it to Logic Layer classes.
        LLAPI also receives information from the Logic Layer which is then displayed on users menu.

    '''
    def __init__(self):
        self.__dapi = DataAPI()
        self.__employee = EmployeeLL(self.__dapi)
        self.__airplane = AirplaneLL(self.__dapi)
        self.__destination = DestinationLL(self.__dapi)
        self.__voyage = VoyageLL(self.__dapi)

#### destination
    def add_destination(self, destination):
        if self.__destination.is_valid_destination(destination):
            self.__destination.add_destination(destination)
            return True

    def get_destination(self):
         return self.__destination.get_destination()

    def update_destination(self, destination, new_contact):
        self.__destination.update_destination(destination, new_contact)
    
#### employee
    def check_if_ssn_unique(self, ssn):
        return self.__employee.check_if_ssn_unique(ssn)

    def is_ssn_valid(self, ssn):
        return self.__employee.is_ssn_valid(ssn)
    
    def add_employee(self, employee):
        if self.__employee.is_valid_employee(employee):
            self.__employee.add_employee(employee)
            return True
    
    def get_employee(self):
        return self.__employee.get_employee()

    def update_employee(self, employee, new_employee):
        self.__employee.update_employee(employee, new_employee)
    
    def get_employee_information(self, employee):
        return self.__employee.get_employee_information(employee)

    def get_employee_by_occupation(self, occupation):
        return self.__employee.get_employee_by_occupation(occupation)
    
    def get_employee_by_status(self, emp_status):
        return self.__employee.get_employee_by_status(emp_status)
        
    def get_pilots_by_airplane(self):
        return self.__employee.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        return self.__employee.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        return self.__employee.get_flight_attendants()

    def get_phone(self, name):
        return self.__employee.get_phone(name)

#### airplane
    def add_airplane(self, airplane):
        if self.__airplane.is_valid_airplane(airplane):
            self.__airplane.add_airplane(airplane)
 
    def get_airplane(self):
        return self.__airplane.get_airplane()

#### voyage
    def add_voyage(self, voyage):
        #if self.is_valid_voyage(voyage):
        self.__voyage.add_voyage(voyage)
 
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        return self.__voyage.get_voyage_destination(voyage_destination, year_int, month_int, day_int)
    
    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        return self.__voyage.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)