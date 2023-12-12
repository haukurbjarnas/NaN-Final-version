from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic
from data.data_wrapper import DataWrapper

class LogicWrapper:
    
    def __init__(self):
        self.employee_logic = EmployeeLogic()
        self.destination_logic = DestinationLogic()
        self.data_wrapper = DataWrapper()

    def add_employee(self, employee):
        '''Adds an employee to csv file'''
        self.employee_logic.add_employee(employee)

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