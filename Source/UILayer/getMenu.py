from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *
import datetime

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
            print_employee_schedule()

    def __get_destination(self):
        print(header_string("GET DESTINATION", 50))
        destination = self.__llapi.get_destination()
        print_destination(destination)


    def __get_airplane_information(self):
        print(header_string("GET AIRPLANE INFORMATION", 50))
        airplanes = self.__llapi.get_airplane()
        print_airplanes(airplanes)

    def __get_voyage(self):
        print(header_string("GET A VOYAGES", 50))
        airport = self.__llapi.get_destination()
        print_airport(airport)
        voyage_destination = input("What voyage would you like to get (insert airport name)? ")
        print("What date are you looking for? (only use numbers)")
        year_int = int(input("Year: "))
        month_int = int(input("Month: "))
        day_int = int(input("Day: "))
        voyages = self.__llapi.get_voyage_destination(voyage_destination, year_int, month_int, day_int)
        print_voyages_destination(voyages, voyage_destination)
        flight_number = input("Please insert flight number for the voyage: ").upper()
        the_voyage = self.__llapi.get_the_voyage(voyage_destination, year_int, month_int, day_int, flight_number)
        print_the_voyage(the_voyage)
        

    def __get_employee_schedule(self):
        print(header_string("GET EMPLOYEE SCHEDULE", 50))
        pass

    def __error_message(self):
        print(header_string('Wrong input, please select from the list!', 100))
        input("\n**   Press any key to return to menu    **")
        
        
