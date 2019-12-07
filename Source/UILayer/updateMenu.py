from LogicLayer.LLAPI import LLAPI

class Update_Menu:

    def __init__(self):
        self.__llapi = LLAPI()
        # self.update_employee_lst = []
        # self.update_destination_lst = []
        # self.update_flight_lst = []

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
            print("2: Update aiport contact info")
            print("3: Update flight")
            print("b: Back")
            # print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "1":
                new_employee = []
                action2 = ""
                self.__update_employee_header()
                employee = input("What employee would you like to update? ")
                print("")
                print("To leave information unchanged press enter")
                new_occupation = input("New occupation: ")
                new_address = input("New address: ")
                new_home_phone = input("New home phone: ")
                new_mobile_phone = input("New mobile phone: ")
                new_email = input("New e-mail: ")
                new_licence = input("New licence: ")
                new_employee.append(new_occupation)
                new_employee.append(new_address)
                new_employee.append(new_home_phone)
                new_employee.append(new_mobile_phone)
                new_employee.append(new_email)
                new_employee.append(new_licence)
                self.__llapi.update_employee(employee, new_employee)
                 

            if action == "2":
                new_contact = []
                action2 = ""
                self.__update_destination_header()
                destination = input("What airport would you like to update? ")
                print("")
                print("What information would you like to update?")
                print("1: Contact name")
                print("2: Contact phone")
                print("3: Both")
                print("")
                action2 = input("Choose an option: ").lower()
                print("")

                if action2 == "1":
                    new_name = input("New contact name: ")
                    new_contact.append(new_name)
                    new_contact.append("")
                elif action2 == "2":
                    new_phone = input("New contact phone: ")
                    new_contact.append("")
                    new_contact.append(new_phone)
                elif action2 == "3":
                    new_name = input("New contact name: ")
                    new_phone = input("New contact phone: ")
                    new_contact.append(new_name)
                    new_contact.append(new_phone)
                    # print(new_contact)
                self.__llapi.update_destination(destination, new_contact)
                
            
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