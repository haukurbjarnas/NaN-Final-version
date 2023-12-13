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
        wants = input("you want to add crew(Y)/(N): ")
        if wants.lower() == "y":
                all_pilots = self.logic_wrapper.list_all_pilots()
                num = 1
                captain_list = []
                for elem in all_pilots:
                    if elem.rank == "Captain":
                        print(f"{num}. {elem.name}")
                        captain_list.append(elem.name)
                        num += 1

                captain_choice = int(input("Select a captain: "))

                captain = captain_list[captain_choice-1]

                all_pilots = self.logic_wrapper.list_all_pilots()
                copilot_list = []
                num2 = 1
                for elem in all_pilots:
                    if elem.rank == "Co-Pilot":
                        print(f"{num2}. {elem.name}")
                        num2 += 1
                        copilot_list.append(elem.name)
                copilot_choice = int(input("Select a co-pilot: "))

                copilot = copilot_list[copilot_choice-1]

                all_attendants = self.logic_wrapper.list_all_attendants()
                num3 = 1
                flight_attendants_list = []
                for elem in all_attendants:
                    print(f"{num3}. {elem.name}")
                    flight_attendants_list.append(elem.name)
                    num3 += 1

                main_choice = int(input("Select flight attendant: "))

                fa1 = flight_attendants_list[main_choice-1]
                all_attendants = self.logic_wrapper.list_all_attendants()
                num4 = 1
                
                for elem in all_attendants:
                    print(f"{num4}. {elem.name}")
                    flight_attendants_list.append(elem.name)
                    num4 += 1

                main_choice_two = int(input("Select flight attendant: "))

                fa2 = flight_attendants_list[main_choice_two-1]
                voyage = Voyage(number_id, flight_nr, flight_nr_two, captain, copilot, fa1, fa2)
                self.logic_wrapper.create_a_voyage(voyage)
        else:
            voyage = Voyage(number_id,flight_nr,flight_nr_two, "", "", "", "")
            self.logic_wrapper.create_a_voyage(voyage)



    def print_all_voyages(self):
        
            pass

    def add_crew_to_voyage(self):
        all_voyages = self.logic_wrapper.get_all_voyages()
        num = 1
        voyage_nr_ids = []
        for voyage in all_voyages:
            print(f"{num}. Voyage id: {voyage.number_id}")
            num += 1

        while True:
            name_of = input("Select voyage: ")
            if name_of.isdigit():
                break
            else:
                print("Invalid input!")
        # for voyage in all_voyages:
        #     print(f"{num}. Voyage ID: {voyage.number_id}")
        #     # voyage_nr_ids.append(voyage.number_id)
        #     num +=1

        # what_voyage = int(input("for what voyage do you want to add crew"))
        # number_id_of_voyage_to_change = all_voyages[what_voyage-1]
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
                captain_list = []
                for elem in all_pilots:
                    if elem.rank == "Captain":
                        print(f"{num}. {elem.name}")
                        captain_list.append(elem.name)
                        num += 1

               

                captain_choice = int(input("Select a captain: "))

                new_info = captain_list[captain_choice-1]
             
                break
            elif wich_crew_to_add == "2":
                update = "copilot"
                all_pilots = self.logic_wrapper.list_all_pilots()
                copilot_list = []
                num2 = 1
                for elem in all_pilots:
                    if elem.rank == "Co-Pilot":
                        print(f"{num2}. {elem.name}")
                        num2 += 1
                        copilot_list.append(elem.name)
                copilot_choice = int(input("Select a co-pilot: "))

                new_info = copilot_list[copilot_choice-1]
                break
            elif wich_crew_to_add == "3":
                update = "fa1"
                all_attendants = self.logic_wrapper.list_all_attendants()
                num3 = 1
                flight_attendants_list = []
                for elem in all_attendants:
                    print(f"{num3}. {elem.name}")
                    flight_attendants_list.append(elem.name)
                    num3 += 1

                main_choice = int(input("Select flight attendant: "))

                new_info = flight_attendants_list[main_choice-1]
                break
            elif wich_crew_to_add == "4":
                update = "fa2"
                all_attendants = self.logic_wrapper.list_all_attendants()
                num4 = 1
                flight_attendants_list = []
                for elem in all_attendants:
                    print(f"{num4}. {elem.name}")
                    flight_attendants_list.append(elem.name)
                    num4 += 1

                main_choice_two = int(input("Select flight attendant: "))

                new_info = flight_attendants_list[main_choice_two-1]
                break
            else:
                print("Invalid input!")

        self.logic_wrapper.add_crew_to_voyage(int(name_of)-1, update, new_info)

        print("Crew member added succesfully!")