from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *
import datetime
import time

class Get_Menu:

    def __init__(self):
        self.__llapi = LLAPI()

    def get_menu(self):
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
        """ TODO Laga menuið eftir að við ákveðum hvernig við höfum þetta """
        print(header_string("GET EMPLOYEE INFORMATION", 50))
        get_employee_information()
        action = input("Choose an option: ").lower()
        if action == "1":
            print(header_string("GET ALL EMPLOYEES", 50))
            employees = self.__llapi.get_employee()
            print_employee(employees)
            press_any_key()
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
            press_any_key()
        elif action == "3":
            print(header_string("GET EMPLOYEES BY OCCUPATION", 50))
            print_employee_by_occupation()
            occupation = input("What occupation would you like to get? ").upper()
            employee_by_occupation = self.__llapi.get_employee_by_occupation(occupation)
            print_employee(employee_by_occupation)
            press_any_key()
        elif action == "4":
            print(header_string("GET EMPLOYEES BY STATUS", 50))
            print_employee_by_status()
            employee_status = input("What status would you like to get? ").upper()
            employee_by_status = self.__llapi.get_employee_by_status(employee_status)
            print_employee(employee_by_status)
            press_any_key()
        elif action == "5":
            print(header_string("GET WEEK SCHEDULE FOR AN EMPLOYEE", 50))
            employee = input("Use SSN for the employee you would like to get the schedule for: ")
            print("\nPlease insert date and you will get the week schedule that includes that date.")
            input_year, input_month, input_day = self.__llapi.get_voyage_date()
            employee_information = self.__llapi.get_employee_information(employee)
            week_dates = self.__llapi.get_week_lst(input_year, input_month, input_day)
            week_schedule_lst = self.__llapi.get_week_schedule(employee, input_year, input_month, input_day)
            print_employee_schedule(employee_information, week_dates, week_schedule_lst)
            press_any_key()
        elif action == "6":
            print(header_string("GET ALL PILOTS BY AIRPLANE MODEL", 50))
            pilots = self.__llapi.get_pilots_by_airplane()
            print_pilots_by_airplane(pilots)
            press_any_key()
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
            press_any_key()

        

    def __get_destination(self):
        print(header_string("GET DESTINATIONS", 50))
        destination = self.__llapi.get_destination()
        print_destination(destination)
        press_any_key()


    def __get_airplane_information(self):
        print(header_string("GET AIRPLANE INFORMATION", 50))
        today = datetime.datetime.now()
        airplanes = self.__llapi.get_airplane(today.year, today.month, today.day, today.hour, today.minute)
        print_airplanes(airplanes)
        press_any_key()

    def __get_voyage(self):
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
        press_any_key()

    def __get_employee_schedule(self):
        print(header_string("GET EMPLOYEE SCHEDULE", 50))
        pass

    def __error_message(self):
        print(header_string('Wrong input, please select from the list!', 100))
        input("\n**   Press any key to return to menu    **")
        
        
