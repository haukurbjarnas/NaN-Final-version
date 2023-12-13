from models.voyage import Voyage
from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI

class VoyageUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.employee_ui = EmployeeUI()

    def voyage_menu(self):
        print("Voyage Management")
        print("1. Create voyage")
        print("2. List all voyages")
        print("3. Add crew to voyage")
        print("")
        print("-"*30)
    
    def input_prompt(self):
        while True:
            print("")
            self.voyage_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                print("")
                self.create_a_voyage()
            elif command == "2":
                print("")
                print("ALL VOYAGES")
                print("-"*40)
                self.print_all_voyages()
            elif command == "3":
                print("")
                self.add_crew_to_voyage()
            elif command == "b":
                print("")
                return "b"
            else:
                print("Invalid input!")

    def create_a_voyage(self):

        all_flights = self.logic_wrapper.get_all_flights()

        num = 1
        for elem in all_flights:
            print(f"{num}. Flight number: {elem.flight_nr}, Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        flight_one_choice = int(input("Select a flight: "))

        flight_one = all_flights[flight_one_choice-1]

        matching_flights = self.logic_wrapper.get_matching_flights(flight_one)

        num = 1
        print("Here are flights that are matchable with your previously chosen flight:")
        for elem in matching_flights:
            print(f"{num}. Flight number: {elem.flight_nr}, Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        flight_two_choice = int(input("Select a matching flight: "))
        flight_two = matching_flights[flight_two_choice-1]

        assign_pilots = input("Do you want to assign pilots now? (Y)es (N)o: ")
        assign_pilots = assign_pilots.lower()
        if assign_pilots == "y":
            
            self.employee_ui.print_pilots()

        assign_attendants = input("Do you want to assign flight attendants now? (Y)es (N)o: ")
        assign_attendants = assign_attendants.lower()
        if assign_attendants == "y":
            
            self.employee_ui.print_attendants()


    def print_all_voyages(self):
        all_voyages = self.logic_wrapper.get_all_voyages()
        for voyage in all_voyages:
            print(f"Flight from ICE: {voyage.flight_nr}")
            print(f"Flight nr back: {voyage.flight_nr_back}")
            print(f"Captain: {voyage.captain}")
            print(f"Copilot: {voyage.copilot}")
            print(f"Flight Attendant 1: {voyage.fa1}")
            print(f"Flight Attendant 2: {voyage.fa2}")
            print("-"*30)
            

    def add_crew_to_voyage(self):
        all_voyages = self.logic_wrapper.get_all_voyages()

        num = 1

        for voyage in all_voyages:
            print(f"{num}. Voyage ID:{voyage.number_id} flight number from iceland: {voyage.flight_nr} flight number back: {voyage.flight_nr_back}")
            num += 1

        while True:
            voyage_number = input("Select number of voyage to change: ")
            if voyage_number.isdigit():
                break
            else:
                print("Invalid input!")
            
        print("Select wich crew member you want to add to the voyage: ")
        print("1. Captain")
        print("2. Copilot")
        print("3. Flight attendant 1")
        print("4. Flight attendant 2")

        wich_crew_to_add = input("Enter number of crew mamber to add: ")

        while True:
            if wich_crew_to_add == "1":
                update = "captain"
                break
            elif wich_crew_to_add == "2":
                update = "copilot"
                break
            elif wich_crew_to_add == "3":
                update = "fa1"
                break
            elif wich_crew_to_add == "4":
                update = "fa2"
                break
            else:
                print("Invalid input!")

        new_info = input("Enter name of crew member:")

        self.logic_wrapper.add_crew_to_voyage(int(wich_crew_to_add)-1, update, new_info)

        print("Crew member added succesfully!")