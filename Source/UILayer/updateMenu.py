from LogicLayer.LLAPI import LLAPI
from models.Voyage import Voyage
from utils.print_functions import *

class Update_Menu:

    def __init__(self):
        self.__llapi = LLAPI()

    def update_menu(self):
        '''Prints the update menu on the screen and asks the user
           to choose an action.'''
        action = ""
        while(action != "b"):
            print(header_string("UPDATE", 50))
            print("1: Update employee")
            print("2: Update airport contact info")
            print("3: Update voyage")
            print("b: Back")
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


            elif action == "3":
                self.__update_voyage()

    def __update_employee(self):
        '''Takes no input. Prints on the screen and asks for input to update/change
           the employee informations that can be changed. There is no output
           printed only saved in the employee.csv data file'''
        new_employee = []
        print(header_string("UPDATE EMPLOYEE", 50))
        emp_to_update = self.__llapi.get_employee()
        print_possible_employee_for_update(emp_to_update)
        employee = input("Social Security Number: ")
        while not(self.__llapi.is_ssn_valid(employee)):
            print("Please insert a valid 10-digit social security number.")
            employee = input("Social Security Number: ")
        if not self.__llapi.check_if_ssn_unique(employee):
            employee_information = self.__llapi.get_employee_information(employee)
            print_employee(employee_information)
            new_occupation = self.__llapi.choose_occupation()
            print("Occupation: ", new_occupation)
            print("")
            print("------------------------------------------")
            print("To leave information unchanged press enter")
            print("------------------------------------------")
            new_address = get_address()
            new_home_phone = self.__llapi.get_phone("Home")
            new_cell_phone = self.__llapi.get_phone("Cell")
            new_email = get_email("update")
            if new_occupation in ["C", "P"]:
                print("")
                print('List of airplane models')
                airplanes = self.__llapi.get_airplanes()
                print_airplane_models(airplanes)
                new_licence = self.__llapi.get_airplane_model("update")
            if is_correct():
                new_employee.extend([new_occupation, new_address, new_home_phone, new_cell_phone, new_email, new_licence])
                self.__llapi.update_employee(employee, new_employee)
                print(header_string("SUCCESS!", 50))
                press_enter()
            else:
                self.__update_employee()
        else:
            print("Employee doesn't exist")
            press_enter()

    def __update_destination(self):
        '''Takes no input. Prints on the screen and asks for input to update/change
           the contact informations for a selected destination. There is no output
           printed only saved in the destination.csv data file'''
        print(header_string("UPDATE DESTINATION", 50))
        new_contact = []
        action2 = ""
        airport = self.__llapi.get_destination()
        print_airport(airport)
        destination = self.__llapi.get_voyage_airport()
        print("")
        print("What information would you like to update?")
        print("1: Contact name")
        print("2: Contact phone")
        print("3: Both")
        print("")
        action2 = input("Choose an option: ").lower()
        print("")

        if action2 == "1":
            new_name = get_string("New contact name")
            new_contact.append(new_name)
            new_contact.append("")
        elif action2 == "2":
            new_phone = self.__llapi.get_phone("New contact")
            new_contact.append("")
            new_contact.append(new_phone)
        elif action2 == "3":
            new_name = get_string("New contact name")
            new_phone = self.__llapi.get_phone("New contact")
            new_contact.append(new_name)
            new_contact.append(new_phone)
        if is_correct():
            print(header_string("SUCCESS!", 50))
            self.__llapi.update_destination(destination, new_contact)
            press_enter()
        else:
            self.__update_destination()

    def __update_voyage(self):
        '''Takes no input. Prints on the screen and asks for input to man a voyage.
           There is no output printed only saved in the voyage.csv data file'''
        print(header_string("MAN A VOYAGE", 50))
        '''Lista upp Destination'''
        airport = self.__llapi.get_destination()
        print_airport(airport)
        voyage_destination = self.__llapi.get_voyage_airport()
        '''Velja dagsetningu'''
        print("What date are you looking for? (only use numbers)")
        year_str, month_str, day_str = self.__llapi.get_voyage_date()
        '''Lista upp ómannaðar voyages'''
        voyages = self.__llapi.get_voyage_destination(voyage_destination, int(year_str), int(month_str), int(day_str))
        '''Láta velja voyage'''
        if print_voyages_destination(voyages, voyage_destination):
            the_voyage_lst = self.__llapi.get_flight_number(voyage_destination, year_str, month_str, day_str)
            the_voyage = the_voyage_lst[0]
        
            airplanes = self.__llapi.get_airplanes()
            for item in airplanes:
                if the_voyage.airplane == item.name:
                    model = item.model
            pilots_model = self.__llapi.get_available_pilots(int(year_str), int(month_str), int(day_str), model)
            print_pilots_by_model(pilots_model)

            captain_str = self.__llapi.get_crew("captain")
            while not self.__llapi.check_occupation("C", captain_str, pilots_model):
                print(not_licensed())
                captain_str = self.__llapi.get_crew("captain") 

            pilot_str = self.__llapi.get_crew("pilot")
            while not self.__llapi.check_occupation("P", pilot_str, pilots_model):
                print(not_licensed())
                pilot_str = self.__llapi.get_crew("pilot")

            flight_attendants = self.__llapi.get_available_crew(int(year_str), int(month_str), int(day_str))
            print_flight_attendants(flight_attendants)

            fsm_str = self.__llapi.get_crew("flight service manager")
            while not self.__llapi.check_occupation("FSM", fsm_str, flight_attendants):
                print(not_licensed())
                fsm_str = self.__llapi.get_crew("flight service manager")
            fa_on_voyage_str = input("Would you like to add a Flight Attendant on this voyage? (Y/N): ").lower()
            while fa_on_voyage_str != "y" and fa_on_voyage_str != "n":
                    print("Wrong input. Please choose Y or N")
                    fa_on_voyage_str = input("Would you like to add a Flight Attendant on this voyage? (Y/N): ").lower()
            if fa_on_voyage_str == "y":
                fa_str = self.__llapi.get_crew("flight attendant")
                while not self.__llapi.check_occupation("FA", fa_str, flight_attendants):
                    print(not_licensed())
                    fa_str = self.__llapi.get_crew("flight attendant")
            else:
                fa_str = "N/A"

            if is_correct():
                print(header_string("SUCCESS!", 50))
                self.__llapi.update_voyage(the_voyage, captain_str, pilot_str, fsm_str, fa_str)
                
            else:
                self.__update_voyage()
        press_enter()