from LogicLayer.Destination_LL import DestinationLL
from LogicLayer.Employee_LL import EmployeeLL
from DataLayer.DataAPI import DataAPI


class LLAPI:
    def __init__(self):
        self.__dapi = DataAPI() #breyta þessu í data_repo
        self.__employee = EmployeeLL(self.__dapi)
        # self.__airplane_repo = DataAPI()
        self.__destination = DestinationLL(self.__dapi)

#### destination
    def add_destination(self, __destination):
        if self.is_valid_destination(__destination):
            self.__destination.add_destination(__destination)

    def get_destinations(self):
         return self.__destination.get_destinations()
    
    def is_valid_destination(self, __destination):
        #here should be some code to 
        #validate the video
        return True

#### employee
    def add_employee(self, __employee):
        if self.is_valid_employee(__employee):
            self.__employee.add_employee(__employee)

    def is_valid_employee(self, employee):
        #add code here to verify
        return True
    
    def get_employee(self):
        return self.__employee.get_employee()

    # def add_destination(self, destination):
    #     if self.is_valid_destination(destination):
    #         self.__destination_repo.add_destination(destination)
    
    # def is_valid_destination(self, destination):
    #     #here should be some code to 
    #     #validate the video
    #     return True

    # def get_destinations(self):
    #     return self.__destination_repo.get_destinations()

    # def get_destinations_by_country(self, country):
    #     pass

#employee föll
    # def add_employee(self, employee):
    #     if self.is_valid_employee(employee):
    #         self.__employee_repo.add_employee(employee)

    # def is_valid_employee(self, employee):
    #     #add code here to verify
    #     return True
    
    # def get_employee(self):
    #     return self.__employee_repo.get_employee()


#airplane föll
    def add_airplane(self, airplane):
        if self.is_valid_airplane(airplane):
            self.__airplane_repo.add_airplane(airplane)
     
    def is_valid_airplane(self, airplane):
        #here should be some code to 
        #validate the video
        return True
 
    def get_airplane(self):
        return self.__airplane_repo.get_airplane()
