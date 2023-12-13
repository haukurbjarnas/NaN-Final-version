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

        flight_number = input("Enter flight number: ")

        all_flights = self.logic_wrapper.get_all_flights()

        num = 1
        
        for elem in all_flights:
            print(elem)
            print(f"{num}. Flight number: {elem.flight_nr}, Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        flight_one_choice = int(input("Select a flight: "))

        flight_one = all_flights[flight_one_choice-1].flight_nr

        print(type(all_flights))

        

        matching_flights = self.logic_wrapper.get_matching_flights(flight_one)

        num = 1
        print("Here are flights that are matchable with your previously chosen flight:")
        for elem in matching_flights:
            print(f"{num}. Flight number: {elem.flight_nr}, Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        flight_two_choice = int(input("Select a matching flight: "))
        flight_two = matching_flights[flight_two_choice-1].flight_nr

        while True:
            assign_crew = input("Do you want to assign crew members now? (Y)es or (N)o: ")
            if assign_crew == "y":
                self.add_crew_to_voyage()
            else:
                break

        voyage = Voyage(flight_number, )


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

        wich_crew_to_add = input("Enter number of crew member to add: ")

        while True:
            
            if wich_crew_to_add == "1":
                update = "captain"
                all_pilots = self.logic_wrapper.list_all_pilots()
                num = 1
                for elem in all_pilots:
                    if elem.rank == "Captain":
                        print(f"{num}. {elem.name}")
                        num += 1

                captain_choice = int(input("Select a captain: "))

                new_info = all_pilots[captain_choice-1].name
                break
            elif wich_crew_to_add == "2":
                update = "copilot"
                all_pilots = self.logic_wrapper.list_all_pilots()
                print(all_pilots)
                num = 1
                for elem in all_pilots:
                    if elem.rank == "Co-Pilot":
                        print(f"{num}. {elem.name}")
                        num += 1

                copilot_choice = int(input("Select a co-pilot: "))

                new_info = all_pilots[copilot_choice-1].name
                break
            elif wich_crew_to_add == "3":
                update = "fa1"
                all_attendants = self.logic_wrapper.list_all_attendants()
                num = 1
                for elem in all_attendants:
                    if elem.rank == "Main flight attendant":
                        print(f"{num}. {elem.name}")
                        num += 1

                main_choice = int(input("Select a Main flight attendant: "))

                new_info = all_pilots[main_choice-1].name
                break
            elif wich_crew_to_add == "4":
                update = "fa2"
                all_attendants = self.logic_wrapper.list_all_attendants()
                num = 1
                for elem in all_attendants:
                    if elem.rank == "Normal Flight attendant":
                        print(f"{num}. {elem.name}")
                        num += 1

                normal_choice = int(input("Select a captain: "))

                new_info = all_attendants[normal_choice-1].name
            else:
                print("Invalid input!")

        self.logic_wrapper.add_crew_to_voyage(int(wich_crew_to_add)-1, update, new_info)

        print("Crew member added succesfully!")