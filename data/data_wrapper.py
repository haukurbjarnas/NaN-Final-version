from data.crew_data import CrewData
from data.destination_data import DestinationData
from data.flight_data import FlightData
from models.crew import Crew

class DataWrapper:
    
    def __init__(self):
        self.crew_data = CrewData()
        self.destination_data = DestinationData()
        self.flight_data = FlightData()

    def create_crew_member(self, crew):
        return self.crew_data.create_crew_member(crew)
    
    def read_all_crew_members(self):
        return self.crew_data.read_all_crew_members()
    
    def update_employee(self, line, coulmn, update):
        self.crew_data.update_csv(line, coulmn, update)

    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    def read_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def create_flight(self, flight):
        self.flight_data.create_flight(flight)

    def read_all_flights(self):
        return self.flight_data.read_all_flights()