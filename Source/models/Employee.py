class Employee:

    def __init__(self, occupation = "", ID = "", name = "", so = "", address = "", home_phone = "", cell_phone = "", email = "", licence = ""):
        self.occupation = occupation
        self.ID = ID
        self.name = name
        self.so = so
        self.address = address
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.email = email
        self.licence = licence

    def get_occupation(self):
        return str(self.occupation)

    def get_id(self):
        return str(self.ID)

    def get_name(self):
        return str(self.name)

    def get_so(self):
        return str(self.so)
        
    def get_address(self):
        return str(self.address)

    def get_home_phone(self):
        return str(self.home_phone)

    def get_cell_phone(self):
        return str(self.cell_phone)

    def get_email(self):
        return str(self.email)
    
    def get_licence(self):
        if self.licence:
            return str(self.licence)
    
    def set_occupation(self, occupation):
        self.occupation = occupation

