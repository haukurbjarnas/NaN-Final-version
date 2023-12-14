from data.data_wrapper import DataWrapper
import csv
class FlightLogic:
    
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

    def create_flight(self, flight):
        self.data_wrapper.create_flight(flight)

    def get_all_flight(self):
        return self.data_wrapper.read_all_flights()
    
    def count_lines_in_csv(self):
        return self.data_wrapper.get_lines_flights()
        