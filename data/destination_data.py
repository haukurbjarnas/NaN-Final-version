import csv
from models.destination import Destination

class DestinationData:
    def __init__(self, file_name="files/destinations.csv"):
        self.file_name = file_name

    def read_all_destinations(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Destination(
                    row["numeric_id"],
                    row["id"],
                    row["country"],
                    row["airport"],
                    row["contact_name"],
                    row["contact_number"],
                    row["distance"]
                ))
        return ret_list
    
    def create_destination(self, destination):

        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["numeric_id", "id", "country", "airport", "contact_name", "contact_number", "distance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                "numeric_id": destination.numeric_id,
                "id": destination.id,
                "country": destination.country,
                "airport": destination.airport,
                "contact_name": destination.contact_name,
                "contact_number": destination.contact_number,
                "distance": destination.distance
            })

    def get_destination_by_id(self, theID):
        allDest = self.read_all_destinations()
        ret = None
        for d in allDest:
            if d.numeric_id == theID:
                ret = d
                break

        return ret
    
    def update_csv(self, row_index, column_name, new_value):
        data = self.read_all_destinations()

        if 0 <= row_index < len(data):
            data[row_index].__dict__[column_name] = new_value
            self.write_csv(data)
            

    def write_csv(self, data):
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["numeric_id", "id", "country", "airport", "contact_name", "contact_number", "distance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for destination in data:
                writer.writerow({
                    "numeric_id": destination.numeric_id,
                    "id": destination.id,
                    "country": destination.country,
                    "airport": destination.airport,
                    "contact_name": destination.contact_name,
                    "contact_number": destination.contact_number,
                    "distance": destination.distance
                })