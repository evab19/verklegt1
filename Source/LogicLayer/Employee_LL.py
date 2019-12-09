from models.Employee import Employee

class EmployeeLL:

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()

    def add_employee(self, employee):
        if self.is_valid_employee(employee):
            self.__employee_repo.add_employee(employee)

    def is_valid_employee(self, employee):
        #add code here to verify
        return True
    
    def get_employee(self):
        return self.__employee_repo.get_employee()

    def update_employee(self, employee, new_employee):
        self.__employee_repo.update_employee(employee, new_employee)
    
    def get_employee_information(self, employee):
        return self.__employee_repo.get_employee_information(employee)
    
    def get_employee_by_occupation(self, occupation):
        return self.__employee_repo.get_employee_by_occupation(occupation)

    def get_employee_by_status(self, emp_status):
        return self.__employee_repo.get_employee_by_status(emp_status)

    def get_pilots_by_airplane(self):
        return self.__employee_repo.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        return self.__employee_repo.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        return self.__employee_repo.get_flight_attendants()
