from models.Employee import Employee
import dateutil.parser
from models.Voyage import Voyage
from DataLayer.Get_DL import Get_DL
from datetime import *
import time
from utils.print_functions import *

class EmployeeLL:

    def __init__(self, dapi_in):
        self.__employee_repo = dapi_in 
        self.__employee = Employee()
        self.__get = Get_DL()

    def choose_occupation(self):
        print_choose_occupation()
        occupation_str = ""
        while True:
            occupation_choice = input("Choose an option: ")
            if occupation_choice == "b":
                return False
            if occupation_choice == "1":
                occupation_str = "C"
                return occupation_str
            elif occupation_choice == "2":
                occupation_str = "P"
                return occupation_str
            elif occupation_choice == "3":
                occupation_str = "FA"
                return occupation_str
            elif occupation_choice == "4":
                occupation_str = "FSM"
                return occupation_str
            else:
                print("Invalid input. Please choose from the list")
        

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



    def check_occupation(self, occupation, ssn):
        employees = self.get_employee()
        for employee in employees:
            if employee.ssn == ssn and employee.occupation == occupation:
                return True
        return False


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
        if name.lower() == "contact" or name.lower() == "new contact":
            print_str = "Please insert a valid phone number"
        else:
            print_str = "Please insert a valid phone number or leave it blank"
        number = input("{} phone: ".format(name))
        while number != "":
            try:
                int(number)
                if len(number) >= 7:
                    return number
                else:
                    print(print_str)
                    number = input("{} phone: ".format(name))
            except ValueError:
                print(print_str)
                number = input("{} phone: ".format(name))
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
        '''Takes call from the UI layer and send it to the Data layer
           so the data can be written to the Data layer.'''
        self.__employee_repo.update_employee(employee, new_employee)
    
    def get_employee_information(self, employee):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__employee_repo.get_employee_information(employee)
    
    def get_employee_by_occupation(self, occupation):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__employee_repo.get_employee_by_occupation(occupation)

    def get_employee_by_status(self, emp_status):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__employee_repo.get_employee_by_status(emp_status)

    def get_pilots_by_airplane(self):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__employee_repo.get_pilots_by_airplane()

    def get_pilots_by_model(self, pilots_model):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
        return self.__employee_repo.get_pilots_by_model(pilots_model)

    def get_flight_attendants(self):
        '''Takes call from the UI layer and sends it to the Data layer
           which returns it to the UI layer to be printed out.'''
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
        year, month, day, hour, minute = parseDate.year, parseDate.month, parseDate.day, parseDate.hour, parseDate.minute
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
