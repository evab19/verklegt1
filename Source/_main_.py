from UILayer.mainMenu import Main_menu

def main():
    '''This is the main function of NaNair booking system

    This booking system is for booking:
    -----------------------------------

    - voyages
    - employees on voyages
    - choose airplanes for each voyage and pilots based on which airplane they are liecenced to fly
    - update employees, airport contact info and update voyages
    - Get lists of destinations, employees, airplanes and voyages
    
    '''
    ui = Main_menu()
    ui.main_menu()

def prufa():
    pass

if __name__ == '__main__':
    main()