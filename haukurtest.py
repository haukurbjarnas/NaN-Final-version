import csv
from models.voyage import Voyage
from data.destination_data import DestinationData
from data.crew_data import CrewData
from models.flight import Flight

class Rassgat:

    def __init__(self, file_name="files/flights.csv"):
        self.file_name = file_name

    def read_all_flights(self):
            '''Reads all flights in the flights csv file and returns it in ret_list'''
            ret_list = []
            with open(self.file_name, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ret_list.append(Flight(
                        row["flight_nr"],
                        DestinationData.get_destination_by_id(row["dep_from"]),
                        DestinationData.get_destination_by_id(row["arr_at"]),
                        row["departure_time"],
                        row["arrival_time"],
                    ))
            return ret_list

hoho = Rassgat()

print(hoho.read_all_flights())