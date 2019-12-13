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
    def add_destination(self, destination):
        '''Takes in input information about a new destination. Calls the correct
           LL class which forwards it to the Data layer.'''
        if self.__destination.is_valid_destination(destination):
            self.__destination.add_destination(destination)
            return True

    def get_destination(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__destination.get_destination()

    def update_destination(self, destination, new_contact):
        '''Takes call from the UI layer and send it to the LL calss which forwards it to the Data layer
           so the data can be written to the Data layer.'''
        return self.__destination.update_destination(destination, new_contact)

    def get_destination_duration(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__destination.get_destination_duration()

    def is_airport_unique(self, airport):
        return self.__destination.is_airport_unique(airport)
    
#### employee

    def choose_occupation(self):
        return self.__employee.choose_occupation()

    def check_if_ssn_unique(self, ssn):
        return self.__employee.check_if_ssn_unique(ssn)

    def is_ssn_valid(self, ssn):
        return self.__employee.is_ssn_valid(ssn)
    
    def check_occupation(self, occupation, ssn, available_lst):
        return self.__employee.check_occupation(occupation, ssn, available_lst)
    
    def add_employee(self, employee):
        '''Takes in input information about a new employee. Calls the correct
           LL class which forwards it to the Data layer.'''
        if self.__employee.is_valid_employee(employee):
            self.__employee.add_employee(employee)
            return True
    
    def get_employee(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_employee()

    def get_available_pilots(self, year, month, day, model):
        return self.__employee.get_available_pilots(year, month, day, model)
    
    def get_available_crew(self, year, month, day):
        return self.__employee.get_available_crew(year, month, day)

    def update_employee(self, employee, new_employee):
        '''Takes call from the UI layer and send it to the LL calss which forwards it to the Data layer
           so the data can be written to the Data layer.'''
        self.__employee.update_employee(employee, new_employee)
    
    def get_employee_information(self, employee):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_employee_information(employee)

    def get_employee_by_occupation(self, occupation):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_employee_by_occupation(occupation)
    
    def get_employee_by_status(self, emp_status):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_employee_by_status(emp_status)
        
    def get_pilots_by_airplane(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_flight_attendants()

    def get_phone(self, name):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_phone(name)

    def get_crew(self, occupation):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_crew(occupation)
        
    def get_week_lst(self, input_year, input_month, input_day):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_start_of_week(input_year, input_month, input_day)

    def get_week_schedule(self, employee, input_year, input_month, input_day):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__employee.get_week_schedule(employee, input_year, input_month, input_day)

#### airplane
    def add_airplane(self, airplane):
        '''Takes in input information about a new airplane. Calls the correct
           LL class which forwards it to the Data layer.'''
        if self.__airplane.is_valid_airplane(airplane):
            self.__airplane.add_airplane(airplane)
 
    def get_airplane(self, year_int, month_int, day_int, hour_int, min_int):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__airplane.get_airplane(year_int, month_int, day_int, hour_int, min_int)
    
    def get_airplanes(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__airplane.get_airplanes()
    
    def get_airplane_status(self, year_int, month_int, day_int):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        empty_list = []
        return self.__airplane.get_airplane_status(year_int, month_int, day_int, 0 ,0, empty_list)
    
    def get_airplane_model(self, status = ""):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__airplane.get_airplane_model(status)

    def is_airplane_unique(self, name_str):
        return self.__airplane.is_airplane_unique(name_str)

#### voyage
    def get_voyage_airport(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_voyage_airport()

    def get_voyage_airplane(self, plane_list):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_voyage_airplane(plane_list)

    def add_voyage(self, voyage):
        '''Takes in input information about a new voyage. Calls the correct
           LL class which forwards it to the Data layer.'''
        self.__voyage.add_voyage(voyage)
 
    def get_voyage_destination(self, voyage_destination, year_int, month_int, day_int):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_voyage_destination(voyage_destination, year_int, month_int, day_int)
    
    def get_the_voyage(self, voyage_destination, year_int, month_int, day_int, flight_number):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)

    def get_all_voyage_at_date(self, year_int, month_int, day_int):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_all_voyage_at_date(year_int, month_int, day_int)
        
    def get_voyage_date(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_voyage_date()

    def get_voyage_time(self):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_voyage_time()
    
    def update_voyage(self, the_voyage, captain_str, pilot_str, fsm_str, fa_str):
        '''Takes call from the UI layer and send it to the LL calss which forwards it to the Data layer
           so the data can be written to the Data layer.'''
        return self.__voyage.update_voyage(the_voyage, captain_str, pilot_str, fsm_str, fa_str)

    def get_flight_number(self, destination, year, month, day):
        '''Takes call from the UI layer and sends it to the correct LL class which
           sends it to the Data layer which returns it to the UI layer to be printed out.'''
        return self.__voyage.get_flight_number(destination, year, month, day)
