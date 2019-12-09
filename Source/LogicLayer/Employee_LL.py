from models.Employee import Employee
class EmployeeLL:

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()

    def add_employee(self, employee):
        if self.is_valid_employee(employee):
            self.__employee_repo.add_employee(employee)
            return True
        else:
            return False

    def is_valid_employee(self, employee):
        if employee.name and employee.occupation and employee.ssn and employee.cell_phone and employee.address != "":
            return True
        else:
            return False

    def check_if_ssn_unique(self, ssn):
        employees = self.get_employee()
        return not(any(employee.ssn == ssn for employee in employees))
    
    def is_ssn_valid(self, ssn):
        if len(ssn) != 10:
            return False
        elif ssn[9] not in ["9","0"]:
            return False
        else:
            try:
                int(ssn)
                return True
            except ValueError:
                return False

    def get_phone(self, name):
        number = input("{} phone: ".format(name))
        while number != "":
            try:
                int(number)
            except ValueError:
                print("Please insert a valid phone number or leave it blank")
                number = input("{} phone: ".format(name))
        
            if len(number) >= 7:
                return number
            else:
                print("Please insert a valid phone number or leave it blank")
                number = input("{} phone: ".format(name))
        else:
            return number
    
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
