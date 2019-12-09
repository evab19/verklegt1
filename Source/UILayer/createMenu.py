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
<<<<<<< HEAD
            elif action == "b":
                pass
            else:
                self.__error_message()
=======
>>>>>>> parent of f01caa6... Merge branch 'Eva' into Thorsteinn


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
            print("Occupation: ", occupation_str)
            name_str = input("Name: ")
            SO_str = input("Social Security Number: ")
            address_str = input("Address: ")
            home_phone_str = input("Home phone: ")
            cell_phone_str = input("Cell phone: ")
            email_str = input("E-mail: ")
            #airplane_license_str = input("Airplane license: ")
            print("")
            correct = input("Is this information correct? (Y/N): ").lower()

            if correct == "y":
                print(header_string("SUCCESS!", 50))
                new_employee = Employee(occupation_str, name_str, SO_str, address_str, home_phone_str, cell_phone_str, email_str)
                self.__llapi.add_employee(new_employee)
<<<<<<< HEAD
            else:
                self.__error_message()
=======
                input("**   Press enter to return to main menu    **")
>>>>>>> parent of f01caa6... Merge branch 'Eva' into Thorsteinn
    
    def __create_destination(self):
        ''' Þurfum við ekki að hafa test á því að inputið sé á
            réttur formatti, t.d. tölustafir þar sem eiga að
            vera tölustafir og e-mail rétt skráð.'''
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
            print(header_string("SUCCESS!", 50))
            new_destination = Destination(country_str, airport_str, duration_str, distance_str, contact_name_str, contact_phone_nr_str)
            self.__llapi.add_destination(new_destination)
            ''' Hér þarf að kalla í API niður í logic layer þar sem inputið
                er sett í rétt format áður en það fer í data layer til 
                skráningar.'''
<<<<<<< HEAD
            print("**   Press enter to return to main menu    **")
=======
            input("**   Press enter to return to main menu    **")
>>>>>>> parent of f01caa6... Merge branch 'Eva' into Thorsteinn
        if correct == "n":
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
            print("**   Press enter to return to main menu    **")
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
<<<<<<< HEAD
            self.__create_voyage()
    
    def __error_message(self):
        print(header_string('WRONG INPUT, please select from the list!', 50))
        input("\n**   Press any key to return to menu    **")
=======
>>>>>>> parent of f01caa6... Merge branch 'Eva' into Thorsteinn

            self.__create_voyage()