from LogicLayer.LLAPI import LLAPI
from models.Voyage import Voyage
from utils.print_functions import *

class Update_Menu:

    def __init__(self):
        self.__llapi = LLAPI()
        # self.update_employee_lst = []
        # self.update_destination_lst = []
        # self.update_flight_lst = []

    def update_menu(self):
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
                self.__update_voyage()

    def __update_employee(self):
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
            new_address = input("New address: ")
            new_home_phone = self.__llapi.get_phone("Home")
            new_cell_phone = self.__llapi.get_phone("Cell")
            new_email = get_email("update")
            if new_occupation in ["C", "P"]:
                print("")
                print('List of airplanes')
                airplanes = self.__llapi.get_airplanes()
                print_airplanes(airplanes)
                new_licence = self.__llapi.get_airplane_model("update")
            if is_correct():
                new_employee.extend([new_occupation, new_address, new_home_phone, new_cell_phone, new_email, new_licence])
                self.__llapi.update_employee(employee, new_employee)
                print(header_string("SUCCESS!", 50))
                press_any_key()
            else:
                self.__update_employee()
        else:
            print("Employee doesn't exist")
            press_any_key()

    def __update_destination(self):
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
            # print(new_contact)
        if is_correct():
            print(header_string("SUCCESS!", 50))
            self.__llapi.update_destination(destination, new_contact)
            press_any_key()
        else:
            self.__update_destination()


    def __update_voyage(self):
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
        pilots_model = self.__llapi.get_pilots_by_model(model)
        print_pilots_by_model(pilots_model)
    
        captain_str = self.__llapi.get_crew("captain")
        while not self.__llapi.check_occupation("C", captain_str):
            print(not_licensed())
            captain_str = self.__llapi.get_crew("captain") 

        pilot_str = self.__llapi.get_crew("pilot")
        while not self.__llapi.check_occupation("P", pilot_str):
            print(not_licensed())
            pilot_str = self.__llapi.get_crew("pilot")

        flight_attendants = self.__llapi.get_flight_attendants()
        print_flight_attendants(flight_attendants)

        fsm_str = self.__llapi.get_crew("flight service manager")
        while not self.__llapi.check_occupation("FSM", fsm_str):
            print(not_licensed())
            fsm_str = self.__llapi.get_crew("flight service manager")
        fa_on_voyage_str = input("Would you like to add a Flight Attendant on this voyage? (Y/N): ").lower()
        #fa_lst = []
        if fa_on_voyage_str == "y": #while í listapælingum
            fa_str = self.__llapi.get_crew("flight attendant")
            while not self.__llapi.check_occupation("FA", fa_str):
                print(not_licensed())
                fa_str = self.__llapi.get_crew("flight attendant")
            #fa_lst.append(fa_str)
            #fa_on_voyage_str = input("Would you like to add another Flight Attendant on this voyage? (Y/N): ").lower()
        else:
            fa_str = "N/A"

        if is_correct():
            print(header_string("SUCCESS!", 50))
            self.__llapi.update_voyage(the_voyage, captain_str, pilot_str, fsm_str, fa_str)
            press_any_key()
        else:
            self.__update_voyage()

        '''Láta uppfæra'''
