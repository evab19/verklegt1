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
            print("1: Create employee")
            print("2: Create destination")
            print("3: Create airplane")
            print("4: Create voyage")
            print("b: Back")
            # print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "1":
                self.__create_employee()
            elif action == "2":
                self.__create_destination()
            elif action == "3":
                self.__create_airplane()
            elif action == "4":
                self.__create_voyage()
            elif action == "b":
                pass
            else:
                self.__error_message()


    def __create_employee(self):
        occupation_choice = ""
        print(header_string("CREATE EMPLOYEE", 50))
        choose_occupation()

        occupation_choice = input("Choose an option: ").lower()
        if occupation_choice == "1":
            occupation_str = "Captain"
        elif occupation_choice == "2":
            occupation_str = "Pilot"
        elif occupation_choice == "3":
            occupation_str = "Flight Attendant"
        elif occupation_choice == "4":
            occupation_str = "Flight Service Manager"
        elif occupation_choice == "b":
            self.create_menu()

        #self.__create_employee_header()
        print("**  Please fill in the information below   **")
        print("")
        print("Occupation: ", occupation_str)
        employee_id_str = occupation_str + str(ID_COUNTER)
        print("ID: ", employee_id_str)
        name_str = input("Name: ")
        SO_str = input("Social Security Number: ")
        address_str = input("Address: ")
        home_phone_str = input("Home phone: ")
        cell_phone_str = input("Cell phone: ")
        email_str = input("E-mail: ")
        if occupation_choice in ["1", "2"]:
            print("")
            print('list of airplanes')
            airplane_license_str = input("Choose airplane: ")
        print("")
        correct = input("Is this information correct? (Y/N): ").lower()

        if correct == "y":
            print(header_string("SUCCESS!", 50))
            new_employee = Employee(occupation_str, employee_id_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str, airplane_license_str)
            self.__llapi.add_employee(new_employee)
        if occupation_choice != "b":

            print("**  Please fill in the information below   **")
            print("")
            print("Occupation: ", occupation_str)
            name_str = input("Name: ")
            SO_str = input("Social Security Number: ")
            if self.__llapi.check_if_ssn_unique(SO_str):
                if self.__llapi.is_ssn_valid(SO_str):
                    address_str = input("Address: ")
                    home_phone_str = self.__llapi.get_phone("Home")
                    cell_phone_str = self.__llapi.get_phone("Cell")
                    email_str = input("E-mail: ")
                    print("")
                    correct = input("Is this information correct? (Y/N): ").lower()

                    if correct == "y":
                        new_employee = Employee(occupation_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str)
                        if self.__llapi.add_employee(new_employee):
                            print(header_string("SUCCESS!", 50))
                            input("\n**   Press any key to return to main menu    **")
                        else:
                            print("Oh-oh something went wrong! Please fill in all information")
                            input("\n**   Press any key to try again    **")
                            self.__create_employee()
                    else:
                        self.__create_employee()
                else:
                    print("Please insert a valid social security number (10 digits)")               
            else:
                print("The SSN aldready exists!")
                input("\n**   Press any key to return to the create menu    **")
            #airplane_license_str = input("Airplane license: ")
    
    def __create_destination(self):
        print(header_string("CREATE DESTINATION", 50))
        print("**  Please fill in the information below   **")
        print("")
        country_str = input("Country: ")
        airport_str = input("Airport: ")
        duration_str = input("Flight duration (hh:mm): ")
        distance_str = input("Distance from Iceland (km): ")
        contact_name_str = input("Contact name: ")
        contact_phone_nr_str = input("Contact emergency phone number: ")
        print("")
        correct = input("Is this information correct? (Y/N): ").lower()

        if correct == "y":
            new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
            if self.__llapi.add_destination(new_destination):
                print(header_string("SUCCESS!", 50))
                input("\n**   Press any key to return to the main menu    **")
            else:
                print("Oh no something went wrong! Please try again.")
                input("\n**   Press any key to try again    **")
                self.__create_destination()
        elif correct == "n":
            self.__create_destination()
        else:
            self.__error_message()

    def __create_airplane(self):
        print(header_string("CREATE AIRPLANE", 50))
        print("**  Please fill in the information below   **")
        print("")
        name_str = input("Name: ")
        model_str = input("Model: ")
        producer_str = input("Producer: ")
        number_of_seats_str = input("Number of seats: ")
        print("")
        correct = input("Is this information correct? (Y/N): ").lower()
 
        if correct == "y":
            print(header_string("SUCCESS!", 50))
            new_airplane = Airplane(name_str, model_str, producer_str, number_of_seats_str)
            self.__llapi.add_airplane(new_airplane)
            input("**   Press enter to return to main menu    **")
        if correct == "n":
            self.__create_airplane()
        else:
            self.__error_message()

    def __create_flight(self):
        print(header_string("CREATE FLIGHT", 50))
        pass

    def __create_voyage(self):
        print(header_string("CREATE VOYAGE", 50))
        print("**  Please fill in the information below   **")
        print("")
        airport = self.__llapi.get_destination()
        print_airport(airport)
        destination_str = input("Destination (airport): ")
        print("Departure date (only use numbers)")
        year_int = int(input("Year: "))
        month_int = int(input("Month: "))
        day_int = int(input("Day: "))
        print("Departure time (Departures from Iceland are between 08:00 and 20:00 (including both),")
        print("four departure times per hour, on minutes 00, 15, 30, and 45)")
        hour_int = int(input("Hour: "))
        minutes_int = int(input("Minutes: "))
        new_departure_time = datetime.datetime(year_int, month_int, day_int, hour_int, minutes_int, 0).isoformat()
        airplanes = self.__llapi.get_airplane()
        print_airplane_name_and_models(airplanes)
        print("Choose an airplane for the voyage, use airplane name")
        airplane_str = input("Airplane (name): ")
        print("")
        man_voyage = input("Would you like to man the voyage at this time? (Y/N): ").lower()

        if man_voyage == "y":
            ''' Prenta lausa flugstjóra'''
            airplanes = self.__llapi.get_airplane()
            for item in airplanes:
                if airplane_str == item.name:
                    model = item.model
            pilots_model = self.__llapi.get_pilots_by_model(model)
            print_pilots_by_model(pilots_model)

            captain_str = input("What Captain should be on this voyage (input SSN)? ")
            ''' Virkni til að setja flugstjóra á voyage'''
            ''' Útbúa villutjékk þannig að aðeins sé hægt að velja occupation C'''

            pilot_str = input("What Pilot should be on this voyage (input SSN)? ")
            ''' Virkni til að setja flugmann á voyage'''
            ''' Útbúa villutjékk þannig að aðeins sé hægt að velja occupation P'''
            
            ''' Prenta lausa FSM '''
            flight_attendants = self.__llapi.get_flight_attendants()
            print_flight_attendants(flight_attendants)
            fsm_str = input("What Flight Service Manager should serve on this voyage (input SSN)? ")
            ''' Virkni til að setja FSM á voyage'''
            fa_on_voyage_str = input("Would you like to add a Fligh Attendant on this woyage? (Y/N): ").lower()

            if fa_on_voyage_str == "y":
                fa_str = input("What Flight Attendant should serve on this voyage (input SSN)? ")
        
        correct = input("Is this information correct? (Y/N): ").lower()
 
        if correct == "y":
            print(header_string("SUCCESS!", 50))
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str, captain_str, pilot_str, fsm_str, fa_str)
            self.__llapi.add_voyage(new_voyage)
            input("**   Press any key to return to main menu    **")
        else:
            self.__create_voyage()
    
    def __error_message(self):
        print(header_string('WRONG INPUT, please select from the list!', 50))
        input("\n**   Press any key to return to menu    **")

