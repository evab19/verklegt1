# from UILayer.mainMenu import Main_menu
from LogicLayer.DestinationAPI import DestinationAPI


class Get_Menu:

    def __init__(self):
        self.__destination_service = DestinationAPI()
        self.__employee_service = DestinationAPI()
        self.__airplane_service = DestinationAPI()

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
                self.__get_employee_header()
                employees = self.__employee_service.get_employee()
                print("{:-<151}".format(""))
                print("{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}".format('| ', 'Occupation', '| ', 'Name', '| ', 'SSN', '| ', 'Address', '| ', 'Home phone', '| ', 'Cell phone', '| ', 'Email', '| ', 'Licence', '|'))
                print("{:-<151}".format(""))
                for item in employees:
                    print(item)
                print("{:-<151}".format(""))
                # print("* C = Captain, P = Pilot, FA = Flight attendant")
                input("\n**   Press enter to return to main menu    **")
            
            elif action == "2":
                self.__get_destination_header()
                destinations = self.__destination_service.get_destinations()
                print("{:-<128}".format(""))
                print("{}{:25}{}{:25}{}{:10}{}{:10}{}{:30}{}{:15}{}".format('| ', 'Country', '| ',  'Airport', '| ', 'Duration', '| ', 'Distance', '| ', 'Contact name', '| ', 'Contact phone', '|'))
                print("{:-<128}".format(""))
                for item in destinations:
                    print(item)
                print("{:-<128}".format(""))
                input("\n**   Press enter to return to main menu    **")

            elif action == "3":
                self.__get_airplane_information_header()
                airplanes = self.__airplane_service.get_airplane()
                print("{:-<94}".format(""))
                print("{}{:20}{}{:20}{}{:25}{}{:20}{}".format('| ', 'Name', '| ',  'Model', '| ', 'Producer', '| ', 'Number of seats', '|'))
                print("{:-<94}".format(""))
                for item in airplanes:
                    print(item)
                print("{:-<94}".format(""))
                input("\n**   Press enter to return to main menu    **")

                #"{}{:20}{}{:20}{}{:25}{}{:20}{}".format('| ', self.name, '| ', self.model, '| ', self.producer, '| ', self.number_of_seats, '|')
    
    def __get_employee_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*               GET EMPLOYEE                *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __get_destination_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*              GET DESTINATION              *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_airplane_information_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*         GET AIRPLANE INFORMATION          *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_flight_schedule_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            GET FLIGHT SCHEDULE            *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __get_employee_schedule_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*         GET EMPLOYEE INFORMATION          *")
        print("*                                           *")
        print("*********************************************")
        print("")

    # def __get_employee(self):
    #     self.__get_employee_header()
    #     pass

    # def __get_destination(self):
    #     self.__get_destination_header()
    #     print("   **    Please insert Airport name     **   ")
    #     print("")
    #     airport_name_str = input("Airport name: ")
    #     ''' Hér kæmi þá virknin sem þarf til að kalla í API, sem
    #         síðan kallar áfram í data layer til að sækja upplýsingar
    #         um þetta destination.'''
    #     ''' Hér kæmi virknin sem þarf til að birta gögnin sem logic
    #         layer API skilar upp.'''
    #     self.__get_destination_header()
    #     print("     **    Destination information    **     ")
    #     print("")
    #     print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
    #     print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
    #     print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
    #     print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
    #     print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
    #     print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
    #     print("")
    #     print("**   Press enter to return to main menu    **")


    # def __get_airplane_information(self):
    #     self.__get_flight_information_header()
    #     print("    **    Please an Airplane name     **     ")
    #     print("")
    #     ''' Hér langar mig að fá lista þannig að hægt sé að velja
    #         rétta flugvél í staðinn fyrir að þurfa að muna nafnið
    #         á vélinni.'''
    #     airplane_name_str = ""
    #     pass

    # def __get_flight_schedule(self):
    #     self.__get_flight_schedule_header()
    #     pass

    # def __get_employee_schedule(self):
    #     self.__get_employee_schedule_header()
    #     pass