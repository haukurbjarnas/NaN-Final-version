from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic 
from logic.voyage_logic import VoyageLogic 
from logic.flight_logic import FlightLogic

from data.data_wrapper import DataWrapper

class LogicWrapper:
    
    def __init__(self):
        self.employee_logic = EmployeeLogic()
        self.destination_logic = DestinationLogic()
        self.data_wrapper = DataWrapper()
        self.voyage_logic = VoyageLogic() 
        self.flight_logic = FlightLogic() 

    def add_employee(self, employee):
        '''Adds an employee to csv file'''
        try:
            self.employee_logic.add_employee(employee)
 
            return {"status": "success"}
        except ValueError as e:
            error_message = str(e)
            if error_message == "Duplicate ID":
                return {"status": "error", "code": "DUPLICATE_ID"}
            elif error_message == "Duplicate Email":
                return {"status": "error", "code": "DUPLICATE_EMAIL"}
            elif error_message == "Duplicate Phone Number":
                return {"status": "error", "code": "DUPLICATE_PHONE"}
            elif error_message == "Duplicate SSN":
                return {"status": "error", "code": "DUPLICATE_SSN"}
            else:
                return {"status": "error", "code": "UNKNOWN_ERROR"}

    def list_all_employees(self):
        '''Gets all employees from the csv file'''
        return self.employee_logic.get_all_employees()
    
    def list_all_pilots(self):
        '''Gets list of all pilots'''
        return self.employee_logic.get_all_pilots()
    
    def list_all_attendants(self):
        '''Gets list all flight attendanst'''
        return self.employee_logic.get_all_flight_attendants()
    
    def get_destination(self, destination):
        self.destination_logic.add_destination(destination)

    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()

    def new_information_employee(self, line, column, update):
        self.employee_logic.update_information_employee(line, column, update)