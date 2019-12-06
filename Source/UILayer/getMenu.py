# from UILayer.mainMenu import Main_menu
from LogicLayer.DestinationAPI import DestinationAPI
from utils.print_functions import header_string


class Get_Menu:

    def __init__(self):
        self.__destination_service = DestinationAPI()
        self.__employee_service = DestinationAPI()
        self.__airplane_service = DestinationAPI()
        # self.get_employee_lst = []
        # self.get_destination_lst = []
        # self.get_flight_info_lst = []
        # self.get_flight_schedule_lst = []
        # self.get_employee_schedule_lst = []

    def get_menu(self):
        action = ""
        while(action != "b"):
            print("")
            print("*********************************************")
            print("*                                           *")
            print("*                   GET                     *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Get employee")
            print("2: Get destination")
            print("3: Get airplane information")
            print("4: Get flight schedule")
            print("5: Get employee schedule")
            print("6: Get pilots by ariplane license")
            print("7: Get pilots by airplane type")
            print("8: Get all airplanes")
            print("b: Back")
            print("")
            # print("q: Quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                employees = self.__employee_service.get_employee()
                print(employees)
                input("\n**   Press enter to return to main menu    **")
            
            elif action == "2":
                destinations = self.__destination_service.get_destinations()
                print(destinations)
                # self.__get_destination()
                input("\n**   Press enter to return to main menu    **")

            elif action == "3":
                print(header_string("GET AIRPLANE INFORMATION", 50))
                airplanes = self.__airplane_service.get_airplane()
                print(airplanes)
                input("\n**   Press enter to return to main menu    **")

    def __get_employee(self):
        print(header_string("GET EMPLOYEE", 50))
        pass

    def __get_destination(self):
        print(header_string("GET DESTINATION", 50))
        print("   **    Please insert Airport name     **   ")
        print("")
        airport_name_str = input("Airport name: ")
        ''' Hér kæmi þá virknin sem þarf til að kalla í API, sem
            síðan kallar áfram í data layer til að sækja upplýsingar
            um þetta destination.'''
        ''' Hér kæmi virknin sem þarf til að birta gögnin sem logic
            layer API skilar upp.'''
        print(header_string("GET DESTINATION", 50))
        print("     **    Destination information    **     ")
        print("")
        print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
        print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
        print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
        print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
        print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
        print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
        print("")
        print("**   Press enter to return to main menu    **")


    def __get_airplane_information(self):
        print(header_string("GET FLIGHT INFORMATION", 50))
        print("    **    Please an Airplane name     **     ")
        print("")
        ''' Hér langar mig að fá lista þannig að hægt sé að velja
            rétta flugvél í staðinn fyrir að þurfa að muna nafnið
            á vélinni.'''
        airplane_name_str = ""
        pass

    def __get_flight_schedule(self):
        print(header_string("GET FLIGHT SCHEDULE", 50))
        pass

    def __get_employee_schedule(self):
        print(header_string("GET EMPLOYEE SCHEDULE", 50))
        pass