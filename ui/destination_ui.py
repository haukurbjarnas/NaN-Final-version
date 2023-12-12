from models.destination import Destination
from logic.logic_wrapper import LogicWrapper

class DestinationUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def destination_menu(self):
        print("Destination Menu")
        print("1. Create destination")
        print("2. List all destinations")
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
            elif command == "b":
                return "b"
            else:
                print("Invalid Input!")


    def create_destination(self):

        while True:
            numeric_id = input("Enter numeric ID: ")
            if numeric_id.isdigit():
                break
            else: 
                print("Invalid input! Only numbers here!")

        while True:
            id = input("Enter destination alphabetic ID: ")
            if id.isalpha():
                break
            else:
                print("Invalid input!")
  
        while True:
            country = input("Enter name of destination (country): ")
            if all(x.isalpha() or x.isspace() for x in country):
                break
            else:
                print("Invalid input!")
        while True:
            airport = input("Enter name of airport: ")
            if all(x.isalpha() or x.isspace() for x in airport):
                break
            else:
                print("Invalid input!")
        while True:        
            contact_name = input("Enter name of contact: ")
            if all(x.isalpha() or x.isspace() for x in contact_name):
                break
            else:
                print("Invalid input!")
        while True:
            contact_number = input(f"Enter {contact_name}'s number: ")
            if contact_number.isdigit():
                break
            else:
                print("Invalid input!")
        while True:
            distance = input(f"Enter distance from Iceland to {airport} in Km: ")
            if distance.isalnum():
                break
            else:
                print("Invalid input!")
        

        destination = Destination(numeric_id, id, country, airport, contact_name, contact_number, distance)
        print("Destination created successfully!")
        self.logic_wrapper.get_destination(destination)

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
            print(f"{dest.contact_name}'s number: {dest.contact_number}")
            print("-"*30)
            print("")