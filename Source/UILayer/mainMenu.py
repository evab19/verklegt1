from UILayer.createMenu import Create_Menu
from UILayer.getMenu import Get_Menu
from UILayer.updateMenu import Update_Menu
from utils.print_functions import header_string

class Main_menu:

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
            elif action == 'q':
                break
            else:
                print(header_string('WRONG INPUT, please select from the list!', 50))
                input("\n**   Press any key to return to menu    **")


   