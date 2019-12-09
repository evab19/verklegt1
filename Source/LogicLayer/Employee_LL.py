from models.Employee import Employee
class EmployeeLL:

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()

    def add_employee(self, __employee):
        if self.is_valid_employee(__employee):
            self.__employee_repo.add_employee(__employee)
            return True
        else:
            return False

    def is_valid_employee(self, __employee):
        self.__ssn = __employee.ssn
        length = len(self.__ssn)
        if __employee.name and __employee.occupation and __employee.ssn and __employee.cell_phone and __employee.address != "":
            if length == 10 and int(self.__ssn):
                return True
            else:
                return False
        else:
            return False
    
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
