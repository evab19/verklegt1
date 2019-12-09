from models.Employee import Employee

class EmployeeLL:
    '''Logic Layer Employee Class

        Logic layer classes receive information from the LLAPI class for processing.
        Information is passed on to IOAPI which interacts with data layer classes

    '''

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()

    def add_employee(self, __employee):
        if self.is_valid_employee(__employee):
            self.__employee_repo.add_employee(__employee)

    def is_valid_employee(self, __employee):
        #add code here to verify
        return True
    
    def get_employee(self):
        return self.__employee_repo.get_employee()

    def update_employee(self, employee, new_employee):
        self.__employee_repo.update_employee(employee, new_employee)
    
    def get_employee_information(self, __employee):
        return self.__employee_repo.get_employee_information(__employee)
    
    def get_employee_by_occupation(self, __occupation):
        return self.__employee_repo.get_employee_by_occupation(__occupation)

    def get_employee_by_status(self, __emp_status):
        return self.__employee_repo.get_employee_by_status(__emp_status)

    def get_pilots_by_airplane(self):
        return self.__employee_repo.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        return self.__employee_repo.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        return self.__employee_repo.get_flight_attendants()
