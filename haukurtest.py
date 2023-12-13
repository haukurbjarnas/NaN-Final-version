from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from models.voyage import Voyage

class RassgatOgRofa:

    def __init__(self):
        self.logic_wrapper = LogicWrapper()
        self.employee_ui = EmployeeUI()
        self.voyage_ui = VoyageUI()

    def create_voyage(self):

        number_id = input("Enter number ID: ")

        all_flights = self.logic_wrapper.get_all_flights()

        num = 1
        for elem in all_flights:
            print(f"{num}. Flight ID: {elem.flight_nr} Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        select_flight_one = int(input("Select flight: "))

        flight_one = all_flights[select_flight_one-1]

        matching_flights = self.logic_wrapper.get_matching_flights(flight_one)

        num = 1
        print("Here are all flights that are matchable with your previously chosen flight:")
        for elem in matching_flights:
            print(f"{num}. Flight ID: {elem.flight_nr} Departing from {elem.dep_from} and arriving at {elem.arr_at}")
            num += 1

        select_flight_two = int(input("Select matchable flight: "))

        flight_two = matching_flights[select_flight_two-1]

        captain = None
        copilot = None
        main = None
        attendant = None

        while True:
            assign_crew = input("Do you want to assign crew now? (Y)es (N)o: ")
            assign_crew = assign_crew.lower()
            if assign_crew == "y":
                    print("1. Captain")
                    print("2. Co-Pilot")
                    print("3. Main flight attendant")
                    print("4. Normal flight attendant")
                    role_to_update = input("Enter role: ")
                    if role_to_update == "1":
                        all_pilots = self.logic_wrapper.list_all_pilots()
                        num = 1
                        for elem in all_pilots:
                            if elem.rank == "Captain":
                                print(f"{num}. {elem.name}")
                                num += 1

                            captain_choice = int(input("Select a captain: "))
                    elif role_to_update == "2":
                        all_pilots = self.logic_wrapper.list_all_pilots()
                        num = 1
                        for elem in all_pilots:
                            if elem.rank == "Co-Pilot":
                                print(f"{num}. {elem.name}")
                                num += 1
                    elif role_to_update == "3":
                        all_attendants = self.logic_wrapper.list_all_attendants()
                        num = 1
                        for elem in all_attendants:
                            if elem.rank == "Main flight attendant":
                                print(f"{num}. {elem.name}")
                                num += 1
                    elif role_to_update == "4":
                        all_attendants = self.logic_wrapper.list_all_attendants()
                        num = 1
                        for elem in all_attendants:
                            if elem.rank == "Normal Flight attendant":
                                print(f"{num}. {elem.name}")
                                num += 1
                    else:
                        print("Invalid input!")
            else:
                break
            

        voyage = Voyage(number_id, flight_one.flight_nr, flight_two.flight_nr, captain, copilot, main, attendant)

        print(voyage)


jaja = RassgatOgRofa()

jaja.create_voyage()



















'''assign_pilots = input("Do you want to assign pilots now? (Y)es (N)o: ")
        assign_pilots = assign_pilots.lower()
        if assign_pilots == "y":
            
            self.employee_ui.print_pilots()

        assign_attendants = input("Do you want to assign flight attendants now? (Y)es (N)o: ")
        assign_attendants = assign_attendants.lower()
        if assign_attendants == "y":
            
            self.employee_ui.print_attendants()'''