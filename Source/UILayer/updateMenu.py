from LogicLayer.LLAPI import LLAPI
from utils.print_functions import *

class Update_Menu:

    def __init__(self):
        self.__llapi = LLAPI()
        # self.update_employee_lst = []
        # self.update_destination_lst = []
        # self.update_flight_lst = []

    def update_menu(self):
        '''Menu for update options

        This class allows the user to choose what to update.
        ----------------------------------------------------
        
            - update_employee = indicates if we would like to update employee information 
            - update_destination = indicates if we would like to update airport contact information
            - update_flight = indicates if we would like to update flight information
            
        '''

        action = ""
        while(action != "b"):
            print(header_string("UPDATE", 50))
            print("1: Update employee")
            print("2: Update airport contact info")
            print("3: Update voyage")
            print("b: Back")
            # print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "1":
                self.__update_employee()
                 
            elif action == "2":
                self.__update_destination()
            elif action == "3":
                pass
            elif action != 'b':
                print(header_string('WRONG INPUT, please select a valid input!',50))
                try_again()


    def __update_employee(self):
        new_employee = []
        print(header_string("UPDATE EMPLOYEE", 50))
        emp_to_update = self.__llapi.get_employee()
        print_possible_employee_for_update(emp_to_update)
        employee = input("Insert SSN of employee you would like to update? ")
        print("")
        print("------------------------------------------")
        print("To leave information unchanged press enter")
        print("------------------------------------------")
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

    def __update_destination(self):
        print(header_string("UPDATE DESTINATION", 50))
        new_contact = []
        action2 = ""
        airport = self.__llapi.get_destination()
        print_airport(airport)
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
        elif action2 != 'b':
            print(header_string('WRONG INPUT, please select a valid input!',50))
            try_again()
        self.__llapi.update_destination(destination, new_contact)


    def __update_flight(self):
        pass

