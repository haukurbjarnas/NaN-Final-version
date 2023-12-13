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
        print("Enter (B)ack to go back")
        print("")
        print("-"*30)
    
    def input_prompt(self):
        while True:
            self.voyage_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.create_a_voyage()
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "b":
                return "b"
            else:
                print("Invalid input!")

    def create_a_voyage(self):

        all_flights = self.logic_wrapper.get_all_flights()

        print(type(all_flights))

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
            
            all_pilots = self.logic_wrapper.list_all_pilots()

            '''Select a captain'''
            num = 1
            for pilot in all_pilots:
                if pilot.role == "Captain":
                    print(f"{num}. {pilot}")
                    num += 1

            captain_choice = input("Select a pilot: ")

            '''Select a co-pilot'''
            for pilot in all_pilots:
                if pilot.role == "Co-Pilot":
                    print(f"{num}. {pilot}")
                    num += 1


        assign_attendants = input("Do you want to assign flight attendants now? (Y)es (N)o: ")
        assign_attendants = assign_attendants.lower()
        if assign_attendants == "y":
            
            all_attendants = self.logic_wrapper.list_all_attendants()

            num = 1
            for attendant in all_attendants:
                print(f"{num}. {attendant}")
                num += 1


    def print_all_voyages(self):

        pass

    def add_crew_to_voyage(self):

        pass