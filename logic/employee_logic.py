from data.data_wrapper import DataWrapper

class EmployeeLogic:
    
    def __init__(self):
        self.crew_wrapper = DataWrapper() 

    def add_employee(self, employee):
        '''Adds an employee to the data base''' 

        employee_error_1 = 1
        employee_error_2 = 2
        employee_error_3 = 3
        employee_error_4 = 4 
        employee_successful = 0

        if self.crew_wrapper.get_crew_member_by_id(employee.nid) != None:
            return employee_error_1  

        elif self.crew_wrapper.get_crew_member_by_email(employee.email) != None: 
            return employee_error_2  

        elif self.crew_wrapper.get_crew_member_by_phone_nr(employee.phone_nr) != None: 
            return employee_error_3 

        elif self.crew_wrapper.get_crew_member_by_ssn(employee.ssn) != None: 
            return employee_error_4

        else: self.crew_wrapper.create_crew_member(employee)
        return employee_successful
        

        

    def get_all_employees(self):
        return self.crew_wrapper.read_all_crew_members()
    
    def get_all_pilots(self):
        pilot_list = []
        crew_list = self.crew_wrapper.read_all_crew_members()
        for elem in crew_list:
            if elem.rank == "Pilot":
                pilot_list.append(f"Name: {elem.name} Rank: {elem.role}") # gæti verið vafasamt brot
        
        return pilot_list
    
    def get_all_flight_attendants(self):
        attendant_list = []
        crew_list = self.crew_wrapper.read_all_crew_members()
        for elem in crew_list:
            if elem.rank == "Flight attendant":
                attendant_list.append(f"Name: {elem.name} Rank: {elem.role}") # gæti verið vafasamt brot

        return attendant_list

    def update_information_employee(self, line, column, update):
        self.crew_wrapper.update_employee(line, column, update)