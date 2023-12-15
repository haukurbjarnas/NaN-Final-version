import csv
from models.voyage import Voyage
from data.destination_data import DestinationData
from data.crew_data import CrewData
from models.flight import Flight

class FlightData:
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
                    row["dep_from"],
                    row["arr_at"],
                    row["departure_time"],
                    row["dep_clock"],
                    row["arrival_time"],
                ))
        return ret_list

    def create_flight(self, flight):
        '''Creates a flight and writes it to the flights csv file'''
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["flight_nr", "dep_from", "arr_at", "departure_time","dep_clock", "arrival_time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'flight_nr' : flight.flight_nr,
                'dep_from': flight.dep_from,
                'arr_at': flight.arr_at,
                'departure_time': flight.departure_time,
                'dep_clock' : flight.dep_clock,
                'arrival_time': flight.arrival_time
            })

    def get_flight_by_id(self, theID):
        allflights = self.read_all_flights()
        ret = None
        for d in allflights:
            if d.fligt_nr == theID:
                ret = d
                break

    def count_lines_in_csv(self):
        with open(self.file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = len(list(csv_reader))
        return line_count