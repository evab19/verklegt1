from UILayer.createMenu import Create_Menu
from UILayer.getMenu import Get_Menu
from UILayer.updateMenu import Update_Menu
from utils.print_functions import header_string
from utils.print_functions import try_again
from datetime import *
import dateutil

class Main_menu:

    '''Main menu for options

        This class allows the user to choose what to update.
        -----------------------------------------------------    
            
            -Create_Menu = if chosen returns create options 
            -Get_Menu = if chosen returns get options
            -Update_Menu = if chosen returns update options

    '''
    #def __init__(self):

    def main_menu(self):       
        action = ""
        while(action != "q"):
            print(header_string("WELCOME TO NaN-AIR!", 50))
            print("1: Create")
            print("2: Get")
            print("3: Update")
            print("q: Quit")
            print("")

            action = input("Choose an option: ").lower()

            if action == "1":
                ui = Create_Menu()
                ui.create_menu()
            elif action == "2":
                ui = Get_Menu()
                ui.get_menu()
            elif action == "3":
                ui = Update_Menu()
                ui.update_menu()
            elif action != 'q':
                print(header_string('WRONG INPUT, please select a valid input!',50))
                try_again()
