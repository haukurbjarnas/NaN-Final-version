from models.flight import Flight
from logic.logic_wrapper import LogicWrapper
import time

class FlightUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def flight_menu(self):
        print("-"*50)
        print("Flight Management")
        print("1. Create flight")
        print("2. List all flights")
        print("(B)ack to go back")
        print("-"*50)
        print("")

    def input_prompt(self):
        while True:
            self.flight_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.create_flight()
            elif command == "2":
                self.print_all_flights()
            elif command == "b":
                return "b"
            else: 
                print("Invalid input try again..")
            

    def create_flight(self):
        flight_nr = f"NAN{self.logic_wrapper.get_lines_flights()}"

        list_of_destinations = self.logic_wrapper.get_all_destinations()

        location_list = []

        num = 1
        for elem in list_of_destinations:
            print(f"{num}. Country: {elem.country} Airport: {elem.airport}")
            location_list.append(elem.id)
            num += 1

        while True:
            selec_place_of_departure = input("Please select place of departure: ")
            if selec_place_of_departure.isdigit() and 1 <= int(selec_place_of_departure) <= len(location_list):
                break
            else:
                print("Invalid input try again..")

        dep_from = location_list[int(selec_place_of_departure) - 1]

        num = 1
        for elem in list_of_destinations:
            print(f"{num}. Country: {elem.country} Airport: {elem.airport}")
            num += 1

        while True:
            select_place_of_arrival = input("Please select place of arrival: ")
            if select_place_of_arrival.isdigit() and 1 <= int(select_place_of_arrival) <= len(location_list):
                break
            else:
                print("Invalid input try again..")

        arr_at = location_list[int(select_place_of_arrival) - 1]

        import datetime

        while True:
            try:
                departure_time = input("Enter date of departure (YYYY M D): ")
      

                dep_clock = input("Enter the time of departure (HH:MM): ")
           

                arrival_time = input("Enter date of arrival (YYYY M D): ")
                
                break

            except ValueError:
                print(f"Invalid input!Please enter dates and times in the specified format.")


        flight = Flight(flight_nr, dep_from, arr_at, departure_time, dep_clock, arrival_time)
        self.logic_wrapper.make_flight(flight)


    def print_all_flights(self):
        
        all_flights = self.logic_wrapper.get_all_flights()

        for elem in all_flights:
            print("-"*50)
            print(f"Flight number: {elem.flight_nr}")
            print(f"Departure from: {elem.dep_from}")
            print(f"Arrival at: {elem.arr_at}")
            print(f"Date and time of departure from {elem.dep_from} (YYYY MM DD HH MM): {elem.departure_time} {elem.dep_clock}")
            print(f"Date of arrival at {elem.arr_at}: {elem.arrival_time}")
            print("-"*50)
            print("")
