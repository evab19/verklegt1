class Destination:

    def __init__(self, country = "", airport = "", duration = "", distance = "", contact_name = "", contact_phone = ""):
        self.country = country
        self.airport = airport
        self.duration = duration
        self.distance = distance
        self.contact_name = contact_name
        self.contact_phone = contact_phone

    def __str__(self):
        return "{}{:25}{}{:25}{}{:10}{}{:10}{}{:30}{}{:15}{}".format('| ', self.country, '| ', self.airport, '| ', self.duration, '| ', self.distance, '| ', self.contact_name, '| ', self.contact_phone, '|')

    def get_country(self):
        return str(self.country)
    
    def get_airport(self):
        return str(self.airport)

    def get_duration(self):
        return str(self.duration)
    
    def get_distance(self):
        return str(self.distance)

    def get_contact_name(self):
        return str(self.contact_name)
    
    def get_contact_phone(self):
        return str(self.contact_phone)