from LogicLayer.LLAPI import LLAPI
from models.Destination import Destination
from models.Employee import Employee
from models.Airplane import Airplane
from models.Voyage import Voyage
from utils.print_functions import header_string

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
                self.__create_voyage()
            elif action == "b":
                pass
            else:
                error_message()


    def __create_employee(self):
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        occupation_choice = ""
        print(header_string("CREATE EMPLOYEE", 50))
        print("** Please choose occupation **")
        print("1: Captain")
        print("2: Pilot")
        print("3: Flight Attendant")
        print("4: Flight Service Manager")
        print("b: Back")
            # print("q: Quit")
        print("")

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

        if occupation_choice != "b":
            print("**  Please fill in the information below   **")
            print("")
            print(please_fill_info())
            print("Occupation: ", occupation_str)
            name_str = input("Name: ")
            SO_str = input("Social Security Number: ")
            address_str = input("Address: ")
            home_phone_str = input("Home phone: ")
            cell_phone_str = input("Cell phone: ")
            email_str = input("E-mail: ")
            while not(self.__llapi.is_ssn_valid(SO_str)):
                print("Please insert a valid 10-digit social security number.")
                SO_str = input("Social Security Number: ")

            if self.__llapi.check_if_ssn_unique(SO_str):
                    address_str = input("Address: ")
                    home_phone_str = self.__llapi.get_phone("Home")
                    cell_phone_str = self.__llapi.get_phone("Cell")
                    email_str = input("E-mail: ")
                    if occupation_choice in ["1", "2"]:
                        print("")
                        print('list of airplanes')
                        airplane_license_str = input("Choose airplane: ")
                    else:
                        airplane_license_str = "N/A"
                    print("")
                    correct = input("Is this information correct? (Y/N): ").lower()

                    if correct == "y":
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
            #airplane_license_str = input("Airplane license: ")
            print("")
            correct = input("Is this information correct? (Y/N): ").lower()

            if correct == "y":
                print(header_string("SUCCESS!", 50))
                new_employee = Employee(occupation_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str)
                self.__llapi.add_employee(new_employee)
                input("**   Press enter to return to main menu    **")
    
    def __create_destination(self):
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
        print(header_string("CREATE DESTINATION", 50))
        print(please_fill_info())
        country_str = input("Country: ")
        airport_str = input("Airport: ")
        duration_str = input("Flight duration (hh:mm): ")
        distance_str = input("Distance from Iceland (km): ")
        contact_name_str = input("Contact name: ")
        contact_phone_nr_str = input("Contact emergency phone number: ")
        print("")
        correct = input("Is this information correct? (Y/N): ").lower()

        if correct == "y":
            print(header_string("SUCCESS!", 50))
            new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
            self.__llapi.add_destination(new_destination)
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
            input("**   Press enter to return to main menu    **")
        if correct == "n":
            if self.__llapi.add_destination(new_destination):
                print(header_string("SUCCESS!", 50))
                input("\n**   Press any key to return to the main menu    **")
            else:
                print("Oh no something went wrong! Please try again.")
                try_again()
                self.__create_destination()
        elif correct == "n":
            self.__create_destination()
        else:
            error_message()

    def __create_airplane(self):
        print(header_string("CREATE AIRPLANE", 50))
        print(please_fill_info())
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
            print("**   Press enter to return to main menu    **")
        if correct == "n":
            self.__create_airplane()
        else:
            error_message()

    def __create_flight(self):
        print(header_string("CREATE FLIGHT", 50))
        pass

    def __create_voyage(self):
        print(header_string("CREATE VOYAGE", 50))
        print("**  Please fill in the information below   **")
        print("")
        destination_str = input("Destination: ")
        date_str = input("Date: ")
        time_str = input("Time: ")
        airplane_str = input("Airplane: ")
        print("")
        correct = input("Is this information correct? (Y/N): ").lower()
 
        if correct == "y":
            print(header_string("SUCCESS!", 50))
            new_voyage = Voyage(destination_str, date_str, time_str, airplane_str)
            self.__llapi.add_voyage(new_voyage)
            input("\n**   Press any key to return to main menu    **")
        else:
        print(please_fill_info())
        airport = self.__llapi.get_destination()
        print_airport(airport)

        destination_str = self.__llapi.get_voyage_airport()
        year_str, month_str, day_str = self.__llapi.get_departure_date()
        hour_str, minutes_str = self.__llapi.get_departure_time()
        new_departure_time = datetime.datetime(int(year_str), int(month_str), int(day_str), int(hour_str), int(minutes_str), 0).isoformat()
       

        availableplanes = self.__llapi.get_airplane_status(int(year_str), int(month_str), int(day_str))
        temp_lst = []
        for item in availableplanes:
            temp_lst.append(item.name)

        print_airplane_name_and_models(availableplanes)
        print("The listed airplanes are available for the given date and time")
        
        air_input = 0
        while air_input != 1:
            airplane_str = input("Airplane (name): ")
            if airplane_str not in temp_lst:
                print("Wrong input or airplane not available")
                print("Please choose an airplane from the list")
            else:
                air_input = 1

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

            captain_str = self.__llapi.get_crew("captain") 
            pilot_str = self.__llapi.get_crew("pilot")

            flight_attendants = self.__llapi.get_flight_attendants()
            print_flight_attendants(flight_attendants)

            fsm_str = self.__llapi.get_crew("flight service manager")
            fa_on_voyage_str = input("Would you like to add a Fligh Attendant on this woyage? (Y/N): ").lower()
            if fa_on_voyage_str == "y":
                fa_str = self.__llapi.get_crew("flight attendant")
            else:
                fa_str = ""
        
            correct = input("Is this information correct? (Y/N): ").lower()
    
            if correct == "y":
                print(header_string("SUCCESS!", 50))
                new_voyage = Voyage(destination_str, new_departure_time, airplane_str, captain_str, pilot_str, fsm_str, fa_str)
                self.__llapi.add_voyage(new_voyage)
                input("**   Press any key to return to main menu    **")
            else:
                self.__create_voyage()
        else:
            new_voyage = Voyage(destination_str, new_departure_time, airplane_str)
            self.__llapi.add_voyage(new_voyage)
    


            self.__create_voyage()