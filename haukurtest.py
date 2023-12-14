from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from models.voyage import Voyage

class RassgatOgRofa:
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
        number_id = input("Enter number id for the voyage: ")
        all_flights = self.logic_wrapper.get_all_flights()
        num = 1
        flight_number_list = []
        for flight in all_flights:
            print(f"{num}. Flight number: {flight.flight_nr} from {flight.dep_from} to {flight.arr_at} Date: {flight.departure_time}")
            num += 1
            flight_number_list.append(flight.flight_nr)
        
        flight_nr_choice = int(input("Select the first flight: "))
        flight_nr = flight_number_list[flight_nr_choice-1]
        num2 = 1
        flight_number_two_list = []
        for flight in all_flights:
            if flight.flight_nr != flight_nr:
                print(f"{num2}. Flight number: {flight.flight_nr} from {flight.dep_from} to {flight.arr_at} Date: {flight.departure_time}")
                num2 += 1
                flight_number_two_list.append(flight.flight_nr)
        
        flight_nr_choice_two = int(input("Select the second flight: "))
        flight_nr_two = flight_number_two_list[flight_nr_choice_two-1]
        voyage = Voyage(num)
        wants = input("you want to add crew now?(Y)/(N)")
        if wants.lower() == "y":
            self.add_crew_to_voyage()



    def print_all_voyages(self):
        
            pass

    def add_crew_to_voyage(self):
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
        
    
            

        


jaja = RassgatOgRofa()

jaja.create_a_voyage()



















'''assign_pilots = input("Do you want to assign pilots now? (Y)es (N)o: ")
        assign_pilots = assign_pilots.lower()
        if assign_pilots == "y":
            
            self.employee_ui.print_pilots()

        assign_attendants = input("Do you want to assign flight attendants now? (Y)es (N)o: ")
        assign_attendants = assign_attendants.lower()
        if assign_attendants == "y":
            
            self.employee_ui.print_attendants()'''