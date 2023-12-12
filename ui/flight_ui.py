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
                pass
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

        departure_time = input("Enter date and time of departure (DD-MM-YY 00:00): ")

        arrival_time = input("Enter date and time of arrival (DD-MM-YY 00:00): ")

        flight = Flight(flight_nr, dep_from, arr_at, departure_time, arrival_time)

        self.logic_wrapper.make_flight(flight)
