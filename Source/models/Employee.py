class Employee:

<<<<<<< Updated upstream
    def __init__(self, occupation = "", ID = "", name = "", ssn = "", address = "", home_phone = "", cell_phone = "", email = "", licence = ""):
=======
    def __init__(self, occupation = "", name = "", ssn = "", address = "", home_phone = "", cell_phone = "", email = "", licence = "", emp_status = "A"):
>>>>>>> Stashed changes
        self.occupation = occupation
        self.ID = ID
        self.name = name
        self.ssn = ssn
        self.address = address
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.email = email
        self.licence = licence
        self.emp_status = emp_status

    def __str__(self):
        return "{}{:13}{}{:25}{}{:12}{}{:20}{}{:12}{}{:12}{}{:30}{}{:10}{}{:10}{}".format('| ', self.occupation, '| ', self.name, '| ', self.ssn, '| ', self.address, '| ', self.home_phone, '| ', self.cell_phone, '| ', self.email, '| ', self.licence, '| ', self.emp_status, '|')

    def get_occupation(self):
        return str(self.occupation)

    def get_id(self):
        return str(self.ID)

    def get_name(self):
        return str(self.name)

    def get_ssn(self):
        return str(self.ssn)
        
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
<<<<<<< Updated upstream
=======
    
    def get_status(self):
        return str(self.status)
    
    def set_occupation(self, occupation):
        self.occupation = occupation
>>>>>>> Stashed changes

