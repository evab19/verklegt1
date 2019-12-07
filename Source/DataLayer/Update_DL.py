from models.Destination import Destination
from models.Airplane import Airplane
from models.Employee import Employee
from models.Voyage import Voyage
import csv

class Update_DL:

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


    def update_employee(self, employee, new_employee):
        with open("./data/employee.csv", newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['occupation', 'id', 'name', 'ssn', 'address', 'home_phone', 'cell_phone', 'email', 'licence']
            reader = csv.DictReader(csvfile)
            with open("./data/tempfile.csv", "w+", encoding='utf-8-sig') as tempfile:
                writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    if row['ssn'] == employee:
                        updated_employee = Employee(row['occupation'], row['name'], row['ssn'], row['address'], row['home_phone'], row['cell_phone'], row['email'], row['licence'])
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
                        row = ({'occupation': updated_employee.occupation, 'name': updated_employee.name, 'ssn': updated_employee.ssn, 'address': updated_employee.address, 'home_phone': updated_employee.home_phone, 'cell_phone': updated_employee.cell_phone, 'email': updated_employee.email, 'licence': updated_employee.licence})
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