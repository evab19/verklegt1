from DataLayer.Get_DL import Get_DL
from DataLayer.Create_DL import Create_DL
import csv

class DataAPI:
    
    def __init__(self):
        self.__get = Get_DL()
        self.__create = Create_DL()
        #bæta við voyage

#### add/create föll
    def add_employee(self, employee):
        return self.__create.add_employee(employee)

    def add_destination(self, destination):
        return self.__create.add_destination(destination)

    def add_airplane(self, airplane):
        return self.__create.add_airplane(airplane)

#### get föll
    def get_employee(self):
        return self.__get.get_employee()
 
    def get_destination(self):
        return self.__get.get_destination()
 
    def get_airplane(self):
        return self.__get.get_airplane()

    def add_voyage(self, voyage):
        destination = voyage.get_destination()
        date = voyage.get_date()
        time = voyage.get_time()
        airplane = voyage.get_airplane()
        with open("./data/voyage.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['destination', 'date', 'time', 'airplane']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'destination': destination, 'date': date, 'time': time, 'airplane': airplane})
        csv_file.close()
 
    def get_voyage(self):
        if self.__voyage == []:
            with open("./data/voyage.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_voyage = Voyage(row['destination'], row['date'], row['time'], row['airplane'])
                    self.__voyage.append(new_voyage)
        return self.__voyage
