from data.data_wrapper import DataWrapper
import csv
class EmployeeLogic:
    
    def __init__(self):
        self.crew_wrapper = DataWrapper()

    def add_employee(self, employee):
        '''Adds an employee to the data base'''
        self.crew_wrapper.create_crew_member(employee)

    def get_all_employees(self):
        return self.crew_wrapper.read_all_crew_members()
    
    def get_all_pilots(self):
        pilot_list = []
        crew_list = self.crew_wrapper.read_all_crew_members()
        for elem in crew_list:
            if elem.role == "Pilot":
                pilot_list.append(elem) 
        
        return pilot_list
    
    def get_all_flight_attendants(self):
        attendant_list = []
        crew_list = self.crew_wrapper.read_all_crew_members()
        for elem in crew_list:
            if elem.role == "Flight attendant":
                attendant_list.append(elem) 

        return attendant_list

    def update_information_employee(self, line, column, update):
        self.crew_wrapper.update_employee(line, column, update)

    def count_lines_in_csv(self):
        return self.crew_wrapper.get_lines_crew()
    

    