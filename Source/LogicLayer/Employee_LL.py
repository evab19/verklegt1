from models.Employee import Employee

class EmployeeLL:

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