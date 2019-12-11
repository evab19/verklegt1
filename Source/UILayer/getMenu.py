from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *
import datetime

class Get_Menu:
    '''Get Option - Menu

        This class allows the user to choose what to he can see/get:
        ------------------------------------------------------------

        -Get_employee = if chosen get a list of employee information 
        -Get_destination = if chosen get a list of destinations
        -Get_airplane = if chosen get airplane information
        -Get_Voyage = if chosen get voyage information
        -back = go back to main menu


    '''
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
            
            elif action != 'b':
                print(header_string('WRONG INPUT, please select a valid input!',50))
                try_again()


    def __get_employee(self):
        """ TODO Laga menuið eftir að við ákveðum hvernig við höfum þetta """
        print(header_string("GET EMPLOYEE INFORMATION", 50))
        get_employee_information()
        action = input("Choose an option: ").lower()
        if action == "1":
            print(header_string("GET ALL EMPLOYEES", 50))
            employees = self.__llapi.get_employee()
            print_employee(employees)
        elif action == "2":
            print(header_string("GET EMPLOYEE INFORMATION", 50))
            employee = input("Use SSN for the employee you would like to get: ")
            employee_information = self.__llapi.get_employee_information(employee)
            print_employee(employee_information)
        elif action == "3":
            print(header_string("GET EMPLOYEES BY OCCUPATION", 50))
            print_employee_by_occupation()
            occupation = input("What occupation would you like to get? ").upper()
            employee_by_occupation = self.__llapi.get_employee_by_occupation(occupation)
            print_employee(employee_by_occupation)
        elif action == "4":
            print(header_string("GET EMPLOYEES BY STATUS", 50))
            print_employee_by_status()
            employee_status = input("What status would you like to get? ").upper()
            employee_by_status = self.__llapi.get_employee_by_status(employee_status)
            print_employee(employee_by_status)
        elif action == "5":
            print(header_string("GET ALL PILOTS BY AIRPLANE MODEL", 50))
            pilots = self.__llapi.get_pilots_by_airplane()
            print_pilots_by_airplane(pilots)
        elif action == "6":
            print(header_string("GET PILOTS BY AN AIRPLANE MODEL", 50))
            airplanes = self.__llapi.get_airplane()
            print_airplane_models(airplanes)
            model_to_find = input("What status would you like to get? ")
            pilots_model = self.__llapi.get_pilots_by_model(model_to_find)
            print_pilots_by_model(pilots_model)
        elif action == "7":
            print(header_string("GET WEEK SCHEDULE FOR AN EMPLOYEE", 50))
            employee = input("Use SSN for the employee you would like to get the schedule for: ")
            print("\nPlease insert date and you will get the week schedule that includes that date.")
            input_year, input_month, input_day = self.__llapi.get_voyage_date()
            employee_information = self.__llapi.get_employee_information(employee)
            week_dates = self.__llapi.get_week_lst(input_year, input_month, input_day)
            week_schedule_lst = self.__llapi.get_week_schedule(employee, input_year, input_month, input_day)
            print_employee_schedule(employee_information, week_dates, week_schedule_lst)
        

    def __get_destination(self):
        print(header_string("GET DESTINATIONS", 50))
        destination = self.__llapi.get_destination()
        print_destination(destination)


    def __get_airplane_information(self):
        print(header_string("GET AIRPLANE INFORMATION", 50))
        airplanes = self.__llapi.get_airplane()
        print_airplanes(airplanes)
        input("\n**   Press any key to return to main menu    **")

    def __get_voyage(self):
        print(header_string("GET VOYAGE INFORMATION", 50))
        airport = self.__llapi.get_destination()
        print_airport(airport)
        voyage_destination = input("What voyage would you like to get (insert airport name)? ")
        print("What date are you looking for? (only use numbers)")
        year_str, month_str, day_str = self.__llapi.get_voyage_date()
        voyages = self.__llapi.get_voyage_destination(voyage_destination, int(year_str), int(month_str), int(day_str))
        if print_voyages_destination(voyages, voyage_destination):
            flight_number = input("Please insert flight number for the voyage: ").upper()
            the_voyage = self.__llapi.get_the_voyage(voyage_destination, int(year_str), int(month_str), int(day_str), flight_number)
            print_the_voyage(the_voyage)
        input("\n**   Press any key to return to main menu    **")
        print("")

    def __get_employee_schedule(self):
        print(header_string("GET EMPLOYEE SCHEDULE", 50))
        pass

        
        
