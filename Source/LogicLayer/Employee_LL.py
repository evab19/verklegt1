from models.Employee import Employee
from models.Voyage import Voyage
from DataLayer.Get_DL import Get_DL
import dateutil.parser
from datetime import *
import time

class EmployeeLL:

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()
        self.__get = Get_DL()

    def add_employee(self, employee):
        if self.is_valid_employee(employee):
            self.__employee_repo.add_employee(employee)

    def is_valid_employee(self, employee):
        #add code here to verify
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

    def get_week_schedule(self, employee, input_year, input_month, input_day):
        dates_of_week = self.get_start_of_week(input_year, input_month, input_day)
        
        schedule_for_employee = self.get_schedule(employee, dates_of_week)

        return schedule_for_employee
    
    def get_input_date_string(self, input_year, input_month, input_day):
        date_weekday = datetime(int(input_year), int(input_month), int(input_day)).isoweekday()
        date_str = str(input_year) + str(input_month) + str(input_day)
        return date_weekday, date_str

    def get_start_of_week(self, input_year, input_month, input_day):
        input_date_weekday, input_date_str = self.get_input_date_string(input_year, input_month, input_day)

        if input_date_weekday == 1:
            dates_of_week = self.get_year_month_day(input_date_str)
        elif input_date_weekday == 2:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-1)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        elif input_date_weekday == 3:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-2)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        elif input_date_weekday == 4:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-3)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        elif input_date_weekday == 5:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-4)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        elif input_date_weekday == 6:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-5)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        elif input_date_weekday == 7:
            temp_date_str = str(((datetime.strptime(input_date_str, "%Y%m%d")) + timedelta(days=-6)).strftime("%Y%m%d"))
            dates_of_week = self.get_year_month_day(temp_date_str)
        return dates_of_week

    def get_year_month_day(self, start_date):
        week_dates_lst = []
        i = 0
        while i < 7:
            week_day_str = str(((datetime.strptime(start_date, "%Y%m%d")) + timedelta(days=i)).strftime("%Y%m%d"))
            week_dates_lst.append(week_day_str)
            i += 1
        return week_dates_lst

    def get_schedule(self, employee, dates_lst):
        schedule_lst = []
        for item in dates_lst:
            dates_year = item[:4]
            dates_month = item[4:6]
            dates_day = item[6:]
            a_voyage = self.__get.get_voyage_by_date_and_employee(employee, int(dates_year), int(dates_month), int(dates_day))
            schedule_lst.append(a_voyage)
        return schedule_lst
