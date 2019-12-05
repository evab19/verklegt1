from models.Destination import Destination
from models.airplane import Plane

class DataAPI:
    
    def __init__(self):
        self.__destinations = []
        self.__airplane = []

    def add_destination(self, destination):
        # first add to file then to private list
        with open("./data/destinations.txt", "a+") as destinations_file:
            country = destination.get_country()
            airport = destination.get_airport()
            duration = destination.get_duration()
            distance = destination.get_distance()
            contact_name = destination.get_contact_name()
            contact_phone = destination.get_contact_phone()
            destinations_file.write("{}, {}, {}, {}, {}, {}\n".format(country, airport, duration, distance, contact_name, contact_phone))
        destinations_file.close()

    def get_destinations(self):
        if self.__destinations == []:
            destinations_str = ""
            # destinations_str = "{}\t\t {}\t\t {}\t\t {}\t\t {}\t\t {}\n".format("Country", "Airport", "Duration", "Distance", "Contact name", "Contact phone")
            with open("./data/destinations.txt", "r") as destination_file:
                for line in destination_file.readlines():
                    country, airport, duration, distance, contact_name, contact_phone = line.split(",")
                    # title, genre, length = line.split(",")
                    destinations_str += "{}, {}, {}, {}, {}, {}".format(country, airport, duration, distance, contact_name, contact_phone)
                    # videos_str += "{}\t\t {}\t\t {}".format(title, genre, length)
                    # new_video = "{}, {}, {}\n".format(title, genre, length)
                    # self.__videos.append(new_video)
        
        return destinations_str
        # return self.__videos



    def add_airplane(self, airplane):
        # first add to file then to private list
        name = airplane.get_name()
        #name = airplane.get_name()
        model = airplane.get_model()
        producer = airplane.get_producer()
        number_of_seats = airplane.get_number_of_seats()
        with open("./data/aircraft.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['name', 'model', 'producer', 'number_of_seats']
            

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'name': name, 'model': model, 'producer': producer, 'number_of_seats': number_of_seats})
        csv_file.close()

    

    def get_airplane(self):
        if self.__airplane == []:
            airplane_str = ""
            with open("./data/aicraft.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['name'] + ', ' + row['model'] + ', ' + row['producer'] + ', ' + row['number_of_seats'])
