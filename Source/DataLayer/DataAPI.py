from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
import csv

class DataAPI:
    
    def __init__(self):
        self.__destinations = []
        self.__employee = []
        self.__airplane = []

    def add_employee(self, employee):
        occupation_str = employee.get_occupation()
        id_str = employee.get_id()
        name_str = employee.get_name()
        ssn_str = employee.get_ssn()
        address_str = employee.get_address()
        home_phone_str = employee.get_home_phone()
        cell_phone_str = employee.get_cell_phone()
        email_str = employee.get_email()
        licence_str = employee.get_licence()
        with open("./data/employee.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['occupation', 'id', 'name', 'ssn', 'address', 'home_phone', 'cell_phone', 'email', 'licence']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'occupation': occupation_str, 'id': id_str, 'name': name_str, 'ssn': ssn_str, 'address': address_str, 'home_phone': home_phone_str, 'cell_phone': cell_phone_str, 'email': email_str, 'licence': licence_str})
        csv_file.close()

    def get_employee(self):
        if self.__employee == []:
            with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_employee = Employee(row['occupation'], row['id'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'])
                    self.__employee.append(new_employee)
        return self.__employee
    
    def update_employee(self, employee, new_employee):
        with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['occupation', 'id', 'name', 'ssn', 'address', 'home_phone', 'cell_phone', 'email', 'licence']
            reader = csv.DictReader(csvfile)
            with open("./data/tempfile.csv", "w+", encoding='utf-8-sig') as tempfile:
                writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['ssn'] == employee:
                        updated_employee = Employee(row['occupation'], row['id'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'])
                        if new_employee[0] != "":
                            updated_employee.occupation = new_employee[0]
                        if new_employee[1] != "":
                            updated_employee.address = new_employee[1]
                        if new_employee[2] != "":
                            updated_employee.home_phone = new_employee[2]
                        if new_employee[3] != "":
                            updated_employee.cell_phone = new_employee[3]
                        if new_employee[4] != "":
                            updated_employee.email = new_employee[4]
                        if new_employee[5] != "":
                            updated_employee.licence = new_employee[5]
                        row = ({'occupation': updated_employee.occupation, 'id': updated_employee.ID, 'name': updated_employee.name, 'ssn': updated_employee.ssn, 'address': updated_employee.address, 'home_phone': updated_employee.home_phone, 'cell_phone': updated_employee.cell_phone, 'email': updated_employee.email, 'licence': updated_employee.licence})
                    writer.writerow(row)
        csvfile.close()
        tempfile.close()

        with open("./data/tempfile.csv", encoding='utf-8-sig') as tempfile:
            reader2 = csv.DictReader(tempfile)
            with open("./data/employee.csv", "w+", encoding='utf-8-sig') as csvfile:
                writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer2.writeheader()
                for row in reader2:
                    writer2.writerow(row)
        tempfile.close()
        csvfile.close()



    def add_destination(self, destination):
        country = destination.get_country()
        airport = destination.get_airport()
        duration = destination.get_duration()
        distance = destination.get_distance()
        contact_name = destination.get_contact_name()
        contact_phone = destination.get_contact_phone()
        with open("./data/destinations.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['country', 'airport', 'duration', 'distance', 'contact_name', 'contact_phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'country': country, 'airport': airport, 'duration': duration, 'distance': distance, 'contact_name': contact_name, 'contact_phone': contact_phone})
        csv_file.close()
 
    def get_destinations(self):
        if self.__destinations == []:
            with open("./data/destinations.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_destination = Destination(row['country'], row['airport'], row['duration'], row['distance'], row['contact_name'], row['contact_phone'])
                    self.__destinations.append(new_destination)
        return self.__destinations
    
    def update_destination(self, destination, new_contact):
        with open("./data/destinations.csv", encoding='utf-8-sig') as csvfile:
            fieldnames = ['country', 'airport', 'duration', 'distance', 'contact_name', 'contact_phone']
            reader = csv.DictReader(csvfile)
            with open("./data/tempfile.csv", "w+", encoding='utf-8-sig') as tempfile:
                writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['airport'] == destination:
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


<<<<<<< Updated upstream
=======
# get föll
    def get_employee(self):
        return self.__get.get_employee()
    
    def get_employee_information(self, employee):
        return self.__get.get_employee_information(employee)

    def get_employee_by_occupation(self, occupation):
        return self.__get.get_employee_by_occupation(occupation)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
    
    def get_employee_by_status(self, emp_status):
        return self.__get.get_employee_by_status(emp_status)
>>>>>>> Stashed changes


    # with open(filename, 'r') as csvfile, tempfile:
    # reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    # for row in reader:
    #     if row['id_str'] == str(employee.get_id()):
    #         row['Name'], row['Course'], row['Year'] = employee.get_name(), employee.ge
    #     row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
    #     writer.writerow(row)

    # shutil.move(tempfile.name, filename)
 
    def add_airplane(self, airplane):
        name = airplane.get_name()
        model = airplane.get_model()
        producer = airplane.get_producer()
        number_of_seats = airplane.get_number_of_seats()
        with open("./data/airplanes.csv", "a+", newline='', encoding='utf-8-sig') as csv_file:
            fieldnames = ['name', 'model', 'producer', 'number_of_seats']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
 
            writer.writerow({'name': name, 'model': model, 'producer': producer, 'number_of_seats': number_of_seats})
        csv_file.close()
 
    def get_airplane(self):
        if self.__airplane == []:
            with open("./data/airplanes.csv", newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_airplane = Airplane(row['name'], row['model'], row['producer'], row['number_of_seats'])
                    self.__airplane.append(new_airplane)
        return self.__airplane

    

