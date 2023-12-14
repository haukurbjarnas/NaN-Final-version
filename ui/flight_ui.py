from models.flight import Flight
from logic.logic_wrapper import LogicWrapper
import time

class FlightUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def flight_menu(self):
        print("Flight Management")
        print("1. Create flight")
        print("2. List all flights")
        print("(B)ack to go back")

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
            

    def create_flight(self):

        flight_nr = input("Enter flight number")

        list_of_destinations = self.logic_wrapper.get_all_destinations()

        location_list = []

        num = 1
        for elem in list_of_destinations:
            print(f"{num}. Country: {elem.country} Airport: {elem.airport}")
            location_list.append(elem.airport)
            num += 1

        selec_place_of_departure = input("Please select place of departure: ")
        
        dep_from = location_list[int(selec_place_of_departure)-1]

        num = 1
        for elem in list_of_destinations:
            print(f"{num}. Country: {elem.country} Airport: {elem.airport}")
            num += 1

        select_place_of_arrival = input("Please select place of arrival: ")

        arr_at = location_list[int(select_place_of_arrival)-1]

        departure_time = input("Enter date of departure (YYYY MM DD): ")

        arrival_time = input("Enter date of arrival (YYYY MM DD): ")

        flight = Flight(flight_nr, dep_from, arr_at, departure_time, arrival_time)

        self.logic_wrapper.make_flight(flight)

    def print_all_flights(self):
        
        all_flights = self.logic_wrapper.get_all_flights()

        for elem in all_flights:

            print("")
            print("-"*30)
            print(f"Flight number: {elem.flight_nr}")
            print(f"Departure from: {elem.dep_from}")
            print(f"Arrival at: {elem.arr_at}")
            print(f"Time of departure from {elem.dep_from}: {elem.departure_time}")
            print(f"Time of arrival at {elem.arr_at}: {elem.arrival_time}")
            print("-"*30)
            print("")
