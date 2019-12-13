from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *
import datetime
import time

class Get_Menu:

    def __init__(self):
        self.__llapi = LLAPI()

    def get_menu(self):
        '''Prints the get menu on the screen and asks the user
           to choose an action.'''
        action = ""
        while(action != "b"):
            print(header_string("GET", 50))
            print_get_menu()
            action = input("Choose an option: ").lower()

            if action == "1":
                self.__get_employee()
         
            elif action == "2":
                self.__get_destination()

            elif action == "3":
                self.__get_airplane_information()

            elif action == "4":
                self.__get_voyage()


    def __get_employee(self):
        '''Takes no input. Prints on the screen and asks for what employee information
           the user wants to see. Based on more input the output is printed on the 
           screen after it has been fetched from the data files'''
        print(header_string("GET EMPLOYEE INFORMATION", 50))
        get_employee_information()
        action = input("Choose an option: ").lower()
        if action == "1":
            print(header_string("GET ALL EMPLOYEES", 50))
            employees = self.__llapi.get_employee()
            print_employee(employees)
            press_enter()
        elif action == "2":
            print(header_string("GET EMPLOYEE INFORMATION", 50))
            SO_str = input("Social Security Number for the employee: ")
            while not(self.__llapi.is_ssn_valid(SO_str)):
                print("Please insert a valid 10-digit social security number.")
                SO_str = input("Social Security Number: ")
            if not self.__llapi.check_if_ssn_unique(SO_str):
                employee_information = self.__llapi.get_employee_information(SO_str)
                print_employee(employee_information)
            else:
                print("Employee doesn't exist")
            press_enter()
        elif action == "3":
            print(header_string("GET EMPLOYEES BY OCCUPATION", 50))
            print_employee_by_occupation()
            occupation = input("What occupation would you like to get? ").upper()
            while occupation not in ["C", "P", "FA", "FSM"]:
                print("Invalid input. Please choose an option from the list")
                occupation = input("What occupation would you like to get? ").upper()
            employee_by_occupation = self.__llapi.get_employee_by_occupation(occupation)
            print_employee(employee_by_occupation)
            press_enter()
        elif action == "4":
            print(header_string("GET EMPLOYEES BY STATUS", 50))
            print_employee_by_status()
            employee_status = input("What status would you like to get? ").upper()
            while employee_status not in ["A", "B"]:
                print("Invalid input. Please choose employee status.")
                employee_status = input("What status would you like to get? ").upper()
            employee_by_status = self.__llapi.get_employee_by_status(employee_status)
            print_employee(employee_by_status)
            press_enter()
        elif action == "5":
            check = 0
            print(header_string("GET WEEK SCHEDULE FOR AN EMPLOYEE", 50))
            employee = input("Social Security Number: ")
            while not(self.__llapi.is_ssn_valid(employee)):
                print("Please insert a valid 10-digit social security number.")
                employee = input("Social Security Number: ")

            if not(self.__llapi.check_if_ssn_unique(employee)):
                while check == 0:
                    print("\nPlease insert date and you will get the week schedule that includes that date.")
                    input_year, input_month, input_day = self.__llapi.get_voyage_date()
                    employee_information = self.__llapi.get_employee_information(employee)
                    week_dates = self.__llapi.get_week_lst(input_year, input_month, input_day)
                    week_schedule_lst = self.__llapi.get_week_schedule(employee, input_year, input_month, input_day)
                    if week_schedule_lst:
                        print_employee_schedule(employee_information, week_dates, week_schedule_lst)
                        check += 1
                        press_enter()
                    else:
                        print("Date out of bounds. Please try again.")
            else:
                print("Employee does not exist")
                press_enter()
        elif action == "6":
            print(header_string("GET ALL PILOTS BY AIRPLANE MODEL", 50))
            pilots = self.__llapi.get_pilots_by_airplane()
            print_pilots_by_airplane(pilots)
            press_enter()
        elif action == "7":
            print(header_string("GET PILOTS BY AN AIRPLANE MODEL", 50))
            airplanes = self.__llapi.get_airplanes()
            print_airplane_models(airplanes)
            model_to_find = input("What airplane would you like to get? ")
            pilots_model = self.__llapi.get_pilots_by_model(model_to_find)
            if pilots_model:
                print_pilots_by_model(pilots_model)
            else:
                print("\n" + "No pilots are licenced for that airplane")
            press_enter()

        

    def __get_destination(self):
        '''Takes no input. Prints on the screen information about all destinations that
           NaN air has on its books.'''
        print(header_string("GET DESTINATIONS", 50))
        destination = self.__llapi.get_destination()
        print_destination(destination)
        press_enter()


    def __get_airplane_information(self):
        '''Takes no input. Prints on the screen information about all airplanes that
           NaN air owns and if the are available or not.'''
        print(header_string("GET AIRPLANE INFORMATION", 50))
        today = datetime.datetime.now()
        airplanes = self.__llapi.get_airplane(today.year, today.month, today.day, today.hour, today.minute)
        voyages = self.__llapi.get_all_voyage_at_date(today.year, today.month, today.day)
        voyages_lst = []
        for item in airplanes:
            if item.plane_status == 'Available':
                voyages_lst.append(" ")
            if item.plane_status != 'Available':
                for voyage in voyages:
                    if item.name == voyage.airplane:
                        voyages_lst.append(voyage)
        print_airplanes(airplanes, voyages_lst)
        press_enter()

    def __get_voyage(self):
        '''Takes no input. Prints on the screen and asks for what voyage the
           user wants to see information for. Based on user selection all 
           information about the selected voyage is printed on the screen.'''
        print(header_string("GET VOYAGE INFORMATION", 50))
        airport = self.__llapi.get_destination()
        print_airport(airport)
        voyage_destination = self.__llapi.get_voyage_airport()
        print("What date are you looking for? (only use numbers)")
        year_str, month_str, day_str = self.__llapi.get_voyage_date()
        voyages = self.__llapi.get_voyage_destination(voyage_destination, int(year_str), int(month_str), int(day_str))
        if print_voyages_destination(voyages, voyage_destination):
           voyage = self.__llapi.get_flight_number(voyage_destination, year_str, month_str, day_str)
           print_the_voyage(voyage)
        press_enter()

    def __error_message(self):
        '''Fetches if the input from user is wrong.'''
        print(header_string('Wrong input, please select from the list!', 100))
        press_enter()