class Update_Menu:

    def __init__(self):
        self.update_employee_lst = []
        self.update_destination_lst = []
        self.update_flight_lst = []

    def update_menu(self):
        action = ""
        while(action != "b"):
            print("")
            print("*********************************************")
            print("*                                           *")
            print("*                 UPDATE                    *")
            print("*                                           *")
            print("*********************************************")
            print("")
            print("1: Update employee")
            print("2: Update destination")
            print("3: Update flight")
            print("b: Back")
            # print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "2":
                self.__update_destination()
            
            # else:
            #     action = "q"

    def __update_employee_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*              UPDATE EMPLOYEE              *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __update_destination_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*            UPDATE DESTINATION             *")
        print("*                                           *")
        print("*********************************************")
        print("")
    
    def __update_flight_header(self):
        print("")
        print("*********************************************")
        print("*                                           *")
        print("*               UPDATE FLIGHT               *")
        print("*                                           *")
        print("*********************************************")
        print("")

    def __update_employee(self):
        self.__update_employee_header()
        pass

    def __update_destination(self):
        self.__update_destination_header()
        print("   **    Please insert Airport name     **   ")
        print("")
        airport_name_str = input("Airport name: ")
        ''' Hér þarf að gera ráð fyrir kóðanum til að kalla í 
            API sem síðan sækir gögnin niður í data layer og
            skilar þeim aftur.'''
        self.__update_destination_header()
        print("     **    Destination information    **     ")
        print("")
        print("Country: " + "Grænland") #Breyturnar eru ekki tilbúnar
        print("Airport: " + "Nuuk") #Breyturnar eru ekki tilbúnar
        print("Flight duration: " + "02:30") #Breyturnar eru ekki tilbúnar
        print("Distance from Iceland: " + "1.000 " + "km.") #Breyturnar eru ekki tilbúnar
        print("Contact name: " + "Chuck Norris") #Breyturnar eru ekki tilbúnar
        print("Contact emergency phone number: " + "+11 444-5555") #Breyturnar eru ekki tilbúnar
        print("")
        correct_str = input("Is this the correct Airport? (Y/N): ").lower()

        if correct_str == "y":
            self.__update_destination_header()
            print("*********************************************")
            print("    ** What information would you like to    ")
            print("                 change? **                  ")
            print("")
            print("1: Contact name")
            print("2: Contact emergency phone number")
            print("b: Back")
            print("")
            action = input("Choose an option: ").lower()

    def __update_flight(self):
        self.__update_flight_header()
        pass