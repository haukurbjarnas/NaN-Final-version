
from models.voyage import Voyage
from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI



class VoyageUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.employee_ui = EmployeeUI()

    def voyage_menu(self):
        print("-"*30)
        print("")
        print("Voyage Management")
        print("1. Create voyage")
        print("2. List all voyages")
        print("3. Add crew to voyage")
        print("4. List fully staffed voyages")
        print("5. List understaffed voyages")
        print("6. Check voyages by week")
        print("7. Check voyages by day")
        print("Enter (B)ack to go back")
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
            elif command == "4":
                print("")
                self.fully_staffed_voyages() 
            elif command == "5":
                print("")
                self.understaffed_voyages()
            elif command == "6":
                print("")
                self.check_voyage_per_week()
            elif command == "7":
                print("")
                self.check_voyage_per_day()
            elif command == "b":
                print("")
                return "b"
            else:
                print("Invalid input!")

    def create_a_voyage(self):
        number_id = self.logic_wrapper.get_lines_voyages()
        all_flights = self.logic_wrapper.get_all_flights()
        num = 1
        flight_number_list = []
        
        for flight in all_flights:
            print(f"{num}. Flight number: {flight.flight_nr} from {flight.dep_from} to {flight.arr_at} Date: {flight.departure_time}")
            num += 1
            flight_number_list.append(flight.flight_nr)
        
        while True:
            flight_nr_choice = input("Select the first flight: ")
            if flight_nr_choice.isdigit() and 0 < int(flight_nr_choice) < num:
                break
            else:
                print("Invalid input!")
        flight_nr = all_flights[int(flight_nr_choice)-1].flight_nr
        flight_one_departure = all_flights[int(flight_nr_choice)-1].departure_time
        num2 = 1


        flight_one = all_flights[int(flight_nr_choice)-1]

        matching_flights = self.logic_wrapper.get_matching_flights(flight_one)

        num10 = 1
        for elem in matching_flights:
            print(f"{num10}. Flight number: {elem.flight_nr} departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num10 += 1

        while True:
            flight_nr_choice_two = input("Select the second flight: ")
            if flight_nr_choice_two.isdigit() and 0 < int(flight_nr_choice_two) < num10:
                break
            else:
                print("Invalid input!")
        
        flight_nr_two = matching_flights[int(flight_nr_choice_two)-1].flight_nr
        flight_two_departure = matching_flights[int(flight_nr_choice_two)-1].departure_time
        wants = input("you want to add crew now?(Y)/(N): ")
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

                main_choice_two = int(input("Select a second flight attendant: "))

                fa2 = flight_attendants_list[main_choice_two-1]
                voyage = Voyage(number_id, flight_nr, flight_nr_two, flight_one_departure, flight_two_departure, captain, copilot, fa1, fa2)
                self.logic_wrapper.create_a_voyage(voyage)
                print("Voyage succesfully created with crew!")
        else:
            voyage = Voyage(number_id,flight_nr,flight_nr_two, flight_one_departure, flight_two_departure, "", "", "", "")
            self.logic_wrapper.create_a_voyage(voyage)
            print("Voyage successfully created without crew!")



    def print_all_voyages(self):

        all_voyages = self.logic_wrapper.get_all_voyages()
        
        for voyage in all_voyages:
            print(f"Voyage {voyage.number_id}: Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")

    def add_crew_to_voyage(self):
        all_voyages = self.logic_wrapper.get_all_voyages()
        num = 1
        
        for voyage in all_voyages:
            print(f"{num}. Voyage id: {voyage.number_id}")
            num += 1

        while True:
            name_of = input("Select voyage: ")
            if name_of.isdigit() and 0 < int(name_of) <num:
                break
            else:
                print("Invalid input!")

        voyage_to_assign = all_voyages[int(name_of)-1]
        
        print("Select wich crew member you want to add to the voyage: ")
        print("1. Captain")
        print("2. Copilot")
        print("3. Flight attendant 1")
        print("4. Flight attendant 2")

        wich_crew_to_add = input("Enter number of crew member to add: ")

        
            
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

            while True:
                captain_choice = input("Select a captain: ")
                if captain_choice.isdigit() and 0 < int(captain_choice) <num:
                    new_info = captain_list[int(captain_choice)-1]
                    voyage_same_day_check = self.logic_wrapper.check_day(voyage_to_assign, new_info)
                    if len(voyage_same_day_check) > 0:
                        print("Employee is already assigned to voyage with the same date!")
                    else:
                        break
                else:
                    print("Invalid input!")


        if wich_crew_to_add == "2":
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
                
            new_info = copilot_list[int(copilot_choice)-1]
               
        if wich_crew_to_add == "3":
            update = "fa1"
            all_attendants = self.logic_wrapper.list_all_attendants()
            num3 = 1
            flight_attendants_list = []
            for elem in all_attendants:
                print(f"{num3}. {elem.name}")
                flight_attendants_list.append(elem.name)
                num3 += 1

            main_choice = int(input("Select flight attendant: "))

            new_info = flight_attendants_list[int(main_choice)-1]
          
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

            new_info = flight_attendants_list[int(main_choice_two)-1]
          
        else:
            print("Invalid input!")

        self.logic_wrapper.add_crew_to_voyage(int(name_of)-1, update, new_info)

        print("Crew member added succesfully!")

    def fully_staffed_voyages(self):
        
        staffed = self.logic_wrapper.send_fully_staffed_voyages()
        print("Fully staffed voyages")
        print("-"*40)
        for voyage in staffed:
            print(f"Voyage {voyage.number_id}: Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")

    def understaffed_voyages(self):
        
        understaffed = self.logic_wrapper.send_understaffed_voyages()
        print("Understaffed voyages")
        print("-"*40)
        for voyage in understaffed:
            print(f"Voyage {voyage.number_id}: Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")

    def check_voyage_per_week(self):

        period = input("do not pad with 0 in month and day and seperate with space\nEnter start of weekly period to check (YYYY-M-D): ")

        weekly_voyages = self.logic_wrapper.check_by_week(period)

        for voyage in weekly_voyages:
            if voyage.captain == None or voyage.copilot == None or voyage.fa1 == None or voyage.fa2 == None:
                print("-"*70)
                print("NOT FULLY STAFFED")
                print(f"Voyage: {voyage.number_id} Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")
                
            else:
                print("-"*70)
                print("FULLY STAFFED")
                print(f"Voyage: {voyage.number_id} Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")
                
        print("-"*70)

    def check_voyage_per_day(self):

        day = input("do not pad with 0 in month and day and seperate with space\nEnter day to check (YYYY-M-D): ")

        daily_voyages = self.logic_wrapper.check_by_day(day)

        for voyage in daily_voyages:
            if voyage.captain == None or voyage.copilot == None or voyage.fa1 == None or voyage.fa2 == None:
                print("-"*70)
                print("NOT FULLY STAFFED")
                print(f"Voyage: {voyage.number_id} Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")
                
            else:
                print("-"*70)
                print("FULLY STAFFED")
                print(f"Voyage: {voyage.number_id} Captain: {voyage.captain} Co-Pilot: {voyage.copilot} Flight attendant 1: {voyage.fa1} Flight attendant 2: {voyage.fa2}")
                
        print("-"*70)