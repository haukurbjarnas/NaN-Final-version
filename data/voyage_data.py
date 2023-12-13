import csv
from models.voyage import Voyage
from data.destination_data import DestinationData
from data.crew_data import CrewData
from data.flight_data import FlightData
class Voyage_Data:
    def __init__(self, file_name="files/voyages.csv"):
        self.file_name = file_name

    def read_all_voyages(self):
        '''Reads all voyages in the voyage csv file and returns it in ret_list'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(
                    # FlightData.get_flight_by_id(row["flight_nr"]),
                    # FlightData.get_flight_by_id(row["flight_nr_back"]),
                    # CrewData.get_crew_member_by_id(row["captain"]),
                    # CrewData.get_crew_member_by_id(row["copilot"]),
                    # CrewData.get_crew_member_by_id(row["fa1"]),
                    # CrewData.get_crew_member_by_id(row["fa2"])
                    row["number_id"],
                    row["flight_nr"],
                    row["flight_nr_back"],
                    row["captain"],
                    row["copilot"],
                    row["fa1"],
                    row["fa2"]
                ))
        return ret_list

    def create_voyage(self, voyage):
        '''Creates a voyage and writes it to the voyage csv file'''
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["number_id", "flight_nr", "flight_nr_back", "captain", "copilot", "fa1", "fa2"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'number_id': voyage.number_id,
                'flight_nr': voyage.flight_nr,
                'flight_nr_back': voyage.flight_nr_back,
                'captain': voyage.captain,
                'copilot': voyage.copilot,
                'fa1': voyage.fa1,
                'fa2': voyage.fa2
            })

    def update_csv(self, row_index, column_name, new_value):
        data = self.read_all_voyages()

        if 0 <= row_index < len(data):
            data[row_index].__dict__[column_name] = new_value
            self.write_csv(data)
            

    def write_csv(self, data):
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["number_id", "flight_nr", "flight_nr_back", "captain", "copilot", "fa1", "fa2"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for voyage in data:
                writer.writerow({
                    'number_id': voyage.number_id,
                    'flight_nr': voyage.flight_nr,
                    'flight_nr_back': voyage.flight_nr_back,
                    'captain': voyage.captain,
                    'copilot': voyage.copilot,
                    'fa1': voyage.fa1,
                    'fa2': voyage.fa2
                })