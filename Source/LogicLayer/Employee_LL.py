from models.Employee import Employee
from datetime import date
import dateutil.parser

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
                if len(number) >= 7:
                    return number
                else:
                    print("Please insert a valid phone number or leave it blank")
                    number = input("{} phone: ".format(name))
            except ValueError:
                print("Please insert a valid phone number or leave it blank")
                number = input("{} phone: ".format(name))
        else:
            return number
    
    def get_employee(self):
        our_employees = self.__employee_repo.get_employee()
        today = date.today()
        available_empl = self.get_employee_status(today.year, today.month, today.day)
        for empl in our_employees:
            for a_empl in available_empl:
                if empl.ssn == a_empl.ssn:
                    empl.emp_status = "A"
                    break
                else:
                    empl.emp_status = "B"
        return our_employees

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

    def get_employee_status(self, year_int, month_int, day_int):
        employees = self.__employee_repo.get_employee()
        voyages_at_same_date = self.__employee_repo.get_all_voyage_at_date(year_int, month_int, day_int)
        available_employees = []
        busy_employees = []
        for voyage in voyages_at_same_date:
            dep_year, dep_month, dep_day = self.parse_date(voyage.departure)
            arr_year, arr_month, arr_day = self.parse_date(voyage.departure)

            if ((dep_year == year_int and dep_month == month_int and dep_day == day_int)
                or (arr_year == year_int and arr_month == month_int and arr_day == day_int)):
                busy_employees.append(voyage.captain)
                busy_employees.append(voyage.pilot)
                busy_employees.append(voyage.flight_attendant)
                busy_employees.append(voyage.fsm)
        
        for employee in employees:
            if employee.ssn not in busy_employees:
                available_employees.append(employee)
        return available_employees

    def parse_date(self, date):
        parseDate = dateutil.parser.parse(date)
        year, month, day, hour, min = parseDate.year, parseDate.month, parseDate.day, parseDate.hour, parseDate.minute
        return year, month, day

    def get_crew(self, occupation):
        ''' returns the ssn of a valid employee for each role '''
        staff_ssn_str = input("What {} should be on this voyage (input SSN)? ".format(occupation))
        while not(self.is_ssn_valid(staff_ssn_str)):
            print("Please insert a valid 10-digit social security number. ")
            staff_ssn_str = input("What {} should be on this voyage (input SSN)? ".format(occupation))

        while self.check_if_ssn_unique(staff_ssn_str):
            print("This employee does not exist.")
            staff_ssn_str = input("What {} should be on this voyage (input SSN)? ".format(occupation))
        
        else:
            return staff_ssn_str