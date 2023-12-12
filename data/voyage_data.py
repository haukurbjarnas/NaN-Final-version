import csv
from models.voyage import Voyage
from data.destination_data import DestinationData
from data.crew_data import CrewData
from data.flight_data import Flight_Data
class Voyage_Data:
    def init(self):
        self.file_name = "files/voyages.csv"

    def read_all_voyages(self):
        '''Reads all voyages in the voyage csv file and returns it in ret_list'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(
                    Flight_Data.get_flight_by_id(row["flight_nr"]),
                    Flight_Data.get_flight_by_id(row["flight_nr_back"]),
                    CrewData.get_crew_member_by_id(row["captain"]),
                    CrewData.get_crew_member_by_id(row["copilot"]),
                    CrewData.get_crew_member_by_id(row["fa1"]),
                    CrewData.get_crew_member_by_id(row["fa2"])
                ))
        return ret_list

    def create_voyage(self, voyage):
        '''Creates a voyage and writes it to the voyage csv file'''
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["flight_nr", "dep_from", "arr_at", "departure", "arrival", "captain", "copilot", "fa1", "fa2"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'flight_nr': voyage.flight_nr,
                'flight_nr_back': voyage.flight_nr_back,
                'captain': voyage.captain,
                'copilot': voyage.copilot,
                'fa1': voyage.fa1,
                'fa2': voyage.fa2
            })