from LogicLayer.LLAPI import LLAPI
from models.Destination import Destination
from models.Employee import Employee
from models.Airplane import Airplane
from models.Voyage import Voyage
from utils.print_functions import *
import datetime

class Create_Menu:

    def __init__(self):
        self.__llapi = LLAPI()

    def create_menu(self):
        action = ""
        while(action != "b"):
            print(header_string("CREATE", 50))
            print_create_menu()

            action = input("Choose an option: ").lower()

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
            else:
                error_message()


    def __create_employee(self):
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
                    address_str = input("Address: ")
                    home_phone_str = self.__llapi.get_phone("Home")
                    cell_phone_str = self.__llapi.get_phone("Cell")
                    email_str = get_email()
                    if occupation_str in ["C", "P"]:
                        print("")
                        print('List of airplanes')
                        airplanes = self.__llapi.get_airplanes()
                        print_airplanes(airplanes)
                        airplane_license_str = self.__llapi.get_airplane_model()
                    else:
                        airplane_license_str = "N/A"
                    print("")

                    if is_correct():
                        new_employee = Employee(occupation_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str, airplane_license_str)
                        if self.__llapi.add_employee(new_employee):
                            print(header_string("SUCCESS!", 50))
                            input("\n**   Press any key to return to main menu    **")
                        else:
                            print("Oh-oh something went wrong! Please fill in all information")
                            try_again()
                            self.__create_employee()
                    else:
                        self.__create_employee()               
            else:
                print("The SSN already exists!")
                input("\n**   Press any key to return to the create menu    **")
    
    def __create_destination(self):
        print(header_string("CREATE DESTINATION", 50))
        print(please_fill_info())
        country_str = get_string("Country")
        airport_str = get_string("Airport")
        duration_str = self.__llapi.get_destination_duration()
        distance_str = get_number("Distance from Iceland (km)")
        contact_name_str = get_string("Contact name")
        contact_phone_nr_str = self.__llapi.get_phone("Contact")
        print("")

        if is_correct():
            new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
            if self.__llapi.add_destination(new_destination):
                print(header_string("SUCCESS!", 50))
                input("\n**   Press any key to return to the main menu    **")
            else:
                print("Oh no something went wrong! Please try again.")
                try_again()
                self.__create_destination()
        else:
            self.__create_destination()

    def __create_airplane(self):
        print(header_string("CREATE AIRPLANE", 50))
        print(please_fill_info())
        name_str = get_string("Name")
        model_str = input("Model: ")
        producer_str = input("Producer: ")
        number_of_seats_str = get_number("Number of seats")
        print("")
        if is_correct():
            print(header_string("SUCCESS!", 50))
            new_airplane = Airplane(name_str, model_str, producer_str, number_of_seats_str)
            self.__llapi.add_airplane(new_airplane)
            input("**   Press enter to return to main menu    **")
        else:
            self.__create_airplane()

    def __new_voyage(self):
        print(header_string("CREATE VOYAGE", 50))
        print(please_fill_info())
        airport = self.__llapi.get_destination()
        print_airport(airport)
        destination_str = self.__llapi.get_voyage_airport()
        copy_voyage = input("\nDo you want to copy an existing voyage? (Y/N): ").lower()
        if copy_voyage == "y":
            self.__copy_voyage(destination_str)
        elif copy_voyage == "n":
            self.__create_voyage(destination_str)

    def __copy_voyage(self, airport):
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
            if man_voyage == "y":
                self.__man_voyage(airport_str, new_departure_time, airplane_str, new_year_str, new_month_str, new_day_str, new_hour_str, new_minutes_str)
            else:
                new_voyage = Voyage(airport_str, new_departure_time, airplane_str)
                self.__llapi.add_voyage(new_voyage)
        else:
            change_employees = input("Would you like to change employees for the voyage? (Y/N): ").lower()
            if change_employees == "y":
                self.__man_voyage(airport_str, new_departure_time, airplane_str, new_year_str, new_month_str, new_day_str, new_hour_str, new_minutes_str)
            else:
                new_voyage = Voyage(airport_str, new_departure_time, airplane_str, copy_voyage.captain, copy_voyage.pilot, copy_voyage.fsm, copy_voyage.flight_attendant)
                self.__llapi.add_voyage(new_voyage)
          
    def __create_voyage(self, destination):
        destination_str = destination
        year_str, month_str, day_str = self.__llapi.get_voyage_date()
        hour_str, minutes_str = self.__llapi.get_voyage_time()
        new_departure_time = datetime.datetime(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str), 0).isoformat()
       
        availableplanes = self.__llapi.get_airplane(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str))
        temp_lst = []
        for item in availableplanes:
            temp_lst.append(item.name)

        print_airplane_name_and_models(availableplanes)
        print("The listed airplanes are available for the given date and time")
        airplane_str = self.__llapi.get_voyage_airplane(temp_lst)
        print("")
        man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()

        if man_voyage == "y":
            self.__man_voyage(destination_str, new_departure_time, airplane_str, year_str, month_str, day_str, hour_str, minutes_str)
        else:
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str)
            self.__llapi.add_voyage(new_voyage)
    
    def __man_voyage(self, destination_str, new_departure_time, airplane_str, year_str, month_str, day_str, hour_str, minutes_str):
        ''' Prenta lausa flugstjóra'''
        airplanes = self.__llapi.get_airplane(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str))
        for item in airplanes:
            if airplane_str == item.name:
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
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str, captain_str, pilot_str, fsm_str, fa_str)
            self.__llapi.add_voyage(new_voyage)
            press_any_key()
        else:
            self.__create_voyage(destination_str)