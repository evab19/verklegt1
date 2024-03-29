from LogicLayer.LLAPI import LLAPI
from models.Destination import Destination
from models.Employee import Employee
from models.Airplane import Airplane
from models.Voyage import Voyage
from utils.print_functions import *
import datetime

class Create_Menu:
    '''Menu for Create options

        This class allows the user to choose what to create.
        -----------------------------------------------------
    
        -create_employee = indicates if we would like to create new employee on the system 
        -create_destination = indicates if we would like to create new destination on the system
        -create_airplane = indicates if we would like to create new airplane on the system
        -create__voyage = indicates if we woule like to create new voyage on the system
        
    '''

    def __init__(self):
        self.__llapi = LLAPI()

    def create_menu(self):
        action = ""
        while(action != "b"):
            print(header_string("CREATE", 50))
            print_create_menu()

            action = input("Choose an option: ").lower()
            while action not in ["1","2","3","4", "b"]:
                print("Invalid input. Please choose from the list")
            if action == "1":
                self.__create_employee()
            elif action == "2":
                self.__create_destination()
            elif action == "3":
                self.__create_airplane()
            elif action == "4":
                self.__new_voyage()
            elif action == "b":
                pass



    def __create_employee(self):
        '''Takes no input. Prints on the screen and asks for input to create
           an employee in the database. If all input is there and correctly
           typed it is saved to the employee.csv data file'''
        print(header_string("CREATE EMPLOYEE", 50))
        occupation_str = self.__llapi.choose_occupation()
        if occupation_str:
            print(please_fill_info())
            print("Occupation: ", occupation_str)
            name_str = get_string("Name")
            SO_str = input("Social Security Number: ")
            while not(self.__llapi.is_ssn_valid(SO_str)):
                print("Please insert a valid 10-digit social security number.")
                SO_str = input("Social Security Number: ")

            if self.__llapi.check_if_ssn_unique(SO_str):
                    address_str = get_address()
                    home_phone_str = self.__llapi.get_phone("Home")
                    cell_phone_str = self.__llapi.get_phone("Cell")
                    email_str = get_email()
                    if occupation_str in ["C", "P"]:
                        print("")
                        print('List of airplane models')
                        airplanes = self.__llapi.get_airplanes()
                        print_airplane_models(airplanes)
                        airplane_license_str = self.__llapi.get_airplane_model()
                    else:
                        airplane_license_str = "N/A"
                    print("")

                    if is_correct():
                        new_employee = Employee(occupation_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str, airplane_license_str)
                        if self.__llapi.add_employee(new_employee):
                            print(header_string("SUCCESS!", 50))
                            press_enter()
                        else:
                            print("Oh-oh something went wrong! Please fill in all information")
                            try_again()
                            self.__create_employee()
                    else:
                        self.__create_employee()               
            else:
                print("The SSN already exists!")
                press_enter()
    
    def __create_destination(self):
        '''Takes no input. Prints on the screen and asks for input to create
           a destination in the database. If all input is there and correctly
           typed it is saved to the destination.csv data file'''
        print(header_string("CREATE DESTINATION", 50))
        print(please_fill_info())
        country_str = get_string("Country")
        airport_str = get_string("Airport")
        if self.__llapi.is_airport_unique(airport_str):    
            duration_str = self.__llapi.get_destination_duration()
            distance_str = get_number("Distance from Iceland (km)")
            contact_name_str = get_string("Contact name")
            contact_phone_nr_str = self.__llapi.get_phone("Contact")
            if is_correct():
                new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
                if self.__llapi.add_destination(new_destination):
                    print(header_string("SUCCESS!", 50))
                    press_enter()
                else:
                    print("Oh no something went wrong! Please try again.")
                    try_again()
                    self.__create_destination()
            else:
                self.__create_destination()
        else:
            print("Airport already exists.")
            press_enter()

    def __create_airplane(self):
        '''Takes no input. Prints on the screen and asks for input to create
           a new airplane in the database. If all input is there and correctly
           typed it is saved to the airplane.csv data file'''
        print(header_string("CREATE AIRPLANE", 50))
        print(please_fill_info())
        name_str = input("Name: ")
        if self.__llapi.is_airplane_unique(name_str):
            model_str = input("Model: ")
            producer_str = input("Producer: ")
            number_of_seats_str = get_number("Number of seats")
            print("")
            if is_correct():
                print(header_string("SUCCESS!", 50))
                new_airplane = Airplane(name_str, model_str, producer_str, number_of_seats_str)
                self.__llapi.add_airplane(new_airplane)
                press_enter()
            else:
                self.__create_airplane()
        else:
            print("Airplane already exists")
            press_enter()

    def __new_voyage(self):
        '''Takes no input. Prints on the screen and asks for input to create
           a new voyage in the database. First step is to input airport name
           and then it calls copy_voyage function if user wants to copy an older
           voyage already in the system. If not it calls the create_voyage
           function.'''
        print(header_string("CREATE VOYAGE", 50))
        print(please_fill_info())
        airport = self.__llapi.get_destination()
        print_airport(airport)
        destination_str = self.__llapi.get_voyage_airport()
        copy_voyage = input("\nDo you want to copy an existing voyage? (Y/N): ").lower()
        while copy_voyage != "y" and copy_voyage != "n":
            print("Wrong input. Please choose Y or N")
            copy_voyage = input("\nDo you want to copy an existing voyage? (Y/N): ").lower()
        if copy_voyage == "y":
            self.__copy_voyage(destination_str)
        else:
            self.__create_voyage(destination_str)

    def __copy_voyage(self, airport):
        '''Takes in a name of the airport that the voyage is scheduled for. Asks for if 
           user wants to man voyage if needed and if user wants to change employees on
           the voyage. Then it writes the new voyage to the voyage.csv file.'''
        print("\nWhat date are you looking for? (only use numbers)")
        airport_str = airport
        copy_year_str, copy_month_str, copy_day_str = self.__llapi.get_voyage_date()
        voyages = self.__llapi.get_voyage_destination(airport, int(copy_year_str), int(copy_month_str), int(copy_day_str))
        if print_voyages_destination(voyages, airport):
            flight_number = input("Please insert flight number for the voyage: ").upper()
            the_voyage = self.__llapi.get_the_voyage(airport, int(copy_year_str), int(copy_month_str), int(copy_day_str), flight_number)
            copy_voyage = the_voyage[0]
        new_year_str, new_month_str, new_day_str = self.__llapi.get_voyage_date()
        print("")
        availableplanes = self.__llapi.get_airplane_status(int(new_year_str), int(new_month_str), int(new_day_str))
        new_hour_str, new_minutes_str = self.__llapi.get_voyage_time()
        new_departure_time = datetime.datetime(int(new_year_str), int(new_month_str), int(new_day_str), int(new_hour_str), int(new_minutes_str), 0).isoformat()
        airplane_str = copy_voyage.airplane

        if copy_voyage.captain == "N/A":
            man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()
            while man_voyage != "y" and man_voyage != "n":
                print("Wrong input. Please choose Y or N")
                man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()
            if man_voyage == "y":
                self.__man_voyage(airport_str, new_departure_time, airplane_str, new_year_str, new_month_str, new_day_str, new_hour_str, new_minutes_str)
            else:
                new_voyage = Voyage(airport_str, new_departure_time, airplane_str)
                self.__llapi.add_voyage(new_voyage)
        else:
            change_employees = input("Would you like to change employees for the voyage? (Y/N): ").lower()
            while change_employees != "y" and change_employees != "n":
                print("Wrong input. Please choose Y or N")
                change_employees = input("Would you like to change employees for the voyage? (Y/N): ").lower()
            if change_employees == "y":
                self.__man_voyage(airport_str, new_departure_time, airplane_str, new_year_str, new_month_str, new_day_str, new_hour_str, new_minutes_str)
            else:
                new_voyage = Voyage(airport_str, new_departure_time, airplane_str, copy_voyage.captain, copy_voyage.pilot, copy_voyage.fsm, copy_voyage.flight_attendant)
                self.__llapi.add_voyage(new_voyage)
          
    def __create_voyage(self, destination):
        '''Takes in a name of the airport that the voyage is scheduled for. Asks for if 
           user wants to man voyage. Then it writes the new voyage to the voyage.csv file.'''
        destination_str = destination
        year_str, month_str, day_str = self.__llapi.get_voyage_date()
        hour_str, minutes_str = self.__llapi.get_voyage_time()
        new_departure_time = datetime.datetime(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str), 0).isoformat()
       

        all_planes = self.__llapi.get_airplane(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str))
        temp_lst = []
        for item in all_planes:
            if item.plane_status == "Available":
                temp_lst.append(item.name)

        print_airplane_name_and_models(all_planes)
        print("The listed airplanes are available for the given date and time")
        airplane_str = self.__llapi.get_voyage_airplane(temp_lst)
        print("")
        man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()
        while man_voyage != "y" and man_voyage != "n":
                print("Wrong input. Please choose Y or N")
                man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()
        if man_voyage == "y":
            self.__man_voyage(destination_str, new_departure_time, airplane_str, year_str, month_str, day_str, hour_str, minutes_str)
        else:
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str)
            self.__llapi.add_voyage(new_voyage)
    
    def __man_voyage(self, destination_str, new_departure_time, airplane_str, year_str, month_str, day_str, hour_str, minutes_str):
        '''Takes in name of airport (destination), departure time, airplane name 
           and date and time to create a new voyage. If all input is valid it
           vill write the voyage to the voyage.csv file.'''
        ''' Prenta lausa flugstjóra'''
        airplanes = self.__llapi.get_airplane(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str))
        for item in airplanes:
            if airplane_str == item.name:
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
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str, captain_str, pilot_str, fsm_str, fa_str)
            self.__llapi.add_voyage(new_voyage)
            press_enter()
        else:
            self.__create_voyage(destination_str)