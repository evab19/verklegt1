from DataLayer.Get_DL import Get_DL
from DataLayer.Create_DL import Create_DL
import csv


class DataAPI:

    def __init__(self):
        self.__get = Get_DL()
        self.__create = Create_DL()

# add/create föll
    def add_employee(self, employee):
        return self.__create.add_employee(employee)

    def add_destination(self, destination):
        return self.__create.add_destination(destination)

    def add_airplane(self, airplane):
        return self.__create.add_airplane(airplane)

    def add_voyage(self, voyage):
        return self.__create.add_voyage(voyage)

# get föll
    def get_employee(self):
        return self.__get.get_employee()

    def get_destination(self):
        return self.__get.get_destination()

    def get_airplane(self):
        return self.__get.get_airplane()

    def get_voyage(self):
        return self.__get.get_voyage()

    def update_destination(self, destination, new_contact):
        with open("./data/destinations.csv", encoding='utf-8-sig') as csvfile:
            fieldnames = ['country', 'airport', 'duration', 'distance', 'contact_name', 'contact_phone']
            reader = csv.DictReader(csvfile)
            with open("./data/tempfile.csv", "w+", encoding='utf-8-sig') as tempfile:
                writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if 
                    row['airport'] == destination:
                        if new_contact[0] == "":
                            updated_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], new_contact[1])
                        elif new_contact[1] == "":
                            updated_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], new_contact[0], row['contact_phone'])
                        else:
                            updated_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], new_contact[0], new_contact[1])
                        row = ({'country': updated_destination.country, 'airport': updated_destination.airport, 'duration': updated_destination.duration, 'distance': updated_destination.distance, 'contact_name': updated_destination.contact_name, 'contact_phone': updated_destination.contact_phone})
                    writer.writerow(row)
        csvfile.close()
        tempfile.close()

        with open("./data/tempfile.csv", encoding='utf-8-sig') as tempfile:
            reader2 = csv.DictReader(tempfile)
            with open("./data/destinations.csv", "w+", encoding='utf-8-sig') as csvfile:
                writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer2.writeheader()
                for row in reader2:
                    writer2.writerow(row)
        tempfile.close()
        csvfile.close()