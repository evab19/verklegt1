from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *


class Get_Menu:

    def __init__(self):
        self.__llapi = LLAPI()

    def get_menu(self):
        action = ""
        while(action != "b"):
            print(header_string("GET", 50))
            get_menu()
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

    def __get_destination(self):
        print(header_string("GET DESTINATION", 50))
        destinations = self.__llapi.get_destinations()
        print_destination(destinations)

        # print("   **    Please insert Airport name     **   ")
        # print("")
        # airport_name_str = input("Airport name: ")
        # ''' Hér kæmi þá virknin sem þarf til að kalla í API, sem
        #     síðan kallar áfram í data layer til að sækja upplýsingar
        #     um þetta destination.'''
        # ''' Hér kæmi virknin sem þarf til að birta gögnin sem logic
        #     layer API skilar upp.'''
        # print(header_string("GET DESTINATION", 50))
        # print("     **    Destination information    **     ")
        # print("")
        # print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
        # print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
        # print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
        # print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
        # print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
        # print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
        # print("")
        # print("**   Press enter to return to main menu    **")


    def __get_airplane_information(self):
        print(header_string("GET AIRPLANE INFORMATION", 50))
        airplanes = self.__llapi.get_airplane()
        print_airplanes(airplanes)
        # print("    **    Please an Airplane name     **     ")
        # print("")
        # ''' Hér langar mig að fá lista þannig að hægt sé að velja
        #     rétta flugvél í staðinn fyrir að þurfa að muna nafnið
        #     á vélinni.'''
        # airplane_name_str = ""

    def __get_voyage(self):
        print(header_string("GET ALL VOYAGES", 50))
        voyages = self.__llapi.get_voyage()
        print_voyages(voyages)

    def __get_employee_schedule(self):
        print(header_string("GET EMPLOYEE SCHEDULE", 50))
        pass
