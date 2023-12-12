import csv
from models.crew import Crew

class CrewData:
    
    def __init__(self, file_name="files/crew.csv"):
        self.file_name = file_name

    def read_all_crew_members(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Crew(
                    row["nid"],
                    row["name"],
                    row["ssn"],
                    row["role"],
                    row["rank"],
                    row["phone_nr"],
                    row["email"],
                    row["address"]
                ))
        return ret_list

    def create_crew_member(self, crew):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "ssn", "role", "rank", "phone_nr", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'nid': crew.nid,
                'name': crew.name,
                'ssn': crew.ssn,
                'role': crew.role,
                'rank': crew.rank,
                'phone_nr': crew.phone_nr,
                'email': crew.email,
                'address': crew.address
            })

    def get_crew_member_by_id(self, theID):
        allcrew = self.read_all_crew_members()
        ret = None
        for d in allcrew:
            if d.nid == theID:
                ret = d
                break
        return ret

    def update_csv(self, row_index, column_name, new_value):
        data = self.read_all_crew_members()

        if 0 <= row_index < len(data):
            data[row_index].__dict__[column_name] = new_value
            self.write_csv(data)
            

    def write_csv(self, data):
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["nid", "name", "ssn", "role", "rank", "phone_nr", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for crew in data:
                writer.writerow({
                    'nid': crew.nid,
                    'name': crew.name,
                    'ssn': crew.ssn,
                    'role': crew.role,
                    'rank': crew.rank,
                    'phone_nr': crew.phone_nr,
                    'email': crew.email,
                    'address': crew.address
                })

