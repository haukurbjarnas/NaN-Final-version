from models.destination import Destination
from logic.logic_wrapper import LogicWrapper

class DestinationUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def destination_menu(self):
        print("Destination Menu")
        print("1. Create destination")
        print("2. List all destinations")
        print("3. Update contact info for destination")
        print("Enter (B)ack to go back")
    def input_prompt(self):
        while True:
            self.destination_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.create_destination()
            elif command == "2":
                self.print_all_destinations()
            elif command == "3":
                self.update_contact_info_for_dest()
            elif command == "b":
                return "b"


    def create_destination(self):
        while True:
            numeric_id = input("Enter numeric ID: ")
            if numeric_id.isdigit():
                break
            else:
                print("Invalid input!")

        while True:
            airport_code = input("Enter Airport abbreviation: ")
            if airport_code.isalpha() and len(airport_code) == 3:
                break
            else:
                print("Invalid input!")

        while True:
            country = input("Enter the country of the destination: ")
            if all(x.isalpha() or x.isspace() for x in country):
                break
            else:
                print("Invalid input!")

        while True:
            airport_name = input("Enter name of the airport: ")
            if all(x.isalpha() or x.isspace() for x in airport_name):
                break
            else:
                print("Invalid input!")

        contact_name = input("Enter a contact name for the destination: ")

        while True:
            contact_number = input(f"Enter {contact_name}'s contact phone number: ")
            if contact_number.isdigit() and 0 < len(contact_number) <= 10:
                break
            else:
                print("Invalid input!")

        while True:
            try:
                distance = int(input(f"Enter distance to {airport_name} in Km: "))
                break
            except ValueError:
                print("Invalid input!")

        destination = Destination(numeric_id, airport_code, country, airport_name, contact_name, contact_number, distance)
        self.logic_wrapper.get_destination(destination)
        print("Destination added succesfully!")

    def print_all_destinations(self):
        
        all_destinations = self.logic_wrapper.get_all_destinations()

        for dest in all_destinations:
            print("")
            print("-"*30)
            print(f"Numeric ID: {dest.numeric_id}")
            print(f"ID: {dest.id}")
            print(f"Country: {dest.country}")
            print(f"Airport: {dest.airport}")
            print(f"Distance to {dest.airport}: {dest.distance}")
            print(f"Name of emergency contact: {dest.contact_name}")
            print(f"{dest.contact_name}'s number : {dest.contact_number}")
            print("-"*30)
            print("")


    def update_contact_info_for_dest(self):
        all_destinations = self.logic_wrapper.get_all_destinations()

        num = 1

        for destination in all_destinations:
            print(f"{num}. {destination.id}")
            num += 1

        while True:
            name_of = input("Select the number of the destination to change: ")
            if name_of.isdigit() and 0 < int(name_of) <num:
                break
            else:
                print("Invalid input!")
            
        print("Select what you want to update: ")
        print("1. Contact name")
        print("2. Contact number")
    

        what_to_update = input("Select what you want to update: ")

        while True:
            if what_to_update == "1":
                update = "contact_name"
                break
            elif what_to_update == "2":
                update = "contact_number"
                break
            else:
                print("Invalid input!")

        while True:
            new_info = input("Enter new info: ")
            if all(x.isalnum() or x.isspace() for x in new_info):
                break
            else:
                print("Invalid input!")

        self.logic_wrapper.new_information_destination(int(name_of)-1, update, new_info)

        print("Update successful...")