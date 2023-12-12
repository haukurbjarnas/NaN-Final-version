from data.crew_data import CrewData
from data.destination_data import DestinationData
from models.crew import Crew

class DataWrapper:
    
    def __init__(self):
        self.crew_data = CrewData()
        self.destination_data = DestinationData()

    def create_crew_member(self, crew):
        self.crew_data.create_crew_member(crew)
    
    def read_all_crew_members(self):
        return self.crew_data.read_all_crew_members()
    
    def update_employee(self, line, coulmn, update):
        self.crew_data.update_csv(line, coulmn, update)

    def create_destination(self, destination):
        self.destination_data.create_destination(destination)
    
    def read_all_destinations(self):
        return self.destination_data.read_all_destinations()