from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic
from logic.flight_logic import FlightLogic
from logic.voyage_logic import VoyageLogic
from logic.schedule_logic import SchedulesLogic
from data.data_wrapper import DataWrapper

class LogicWrapper:
    
    def __init__(self):
        self.employee_logic = EmployeeLogic()
        self.destination_logic = DestinationLogic()
        self.data_wrapper = DataWrapper()
        self.flight_logic = FlightLogic()
        self.voyage_logic = VoyageLogic()
        self.schedules_logic = SchedulesLogic()

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

    def make_flight(self, flight):
        self.flight_logic.create_flight(flight)

    def get_all_flights(self):
        return self.flight_logic.get_all_flight()
    
    def get_matching_flights(self, flight):
        return self.voyage_logic.connected_flights(flight)
    
    def get_all_voyages(self):
        return self.voyage_logic.get_all_voyages()
    
    def new_information_destination(self, line, column, update):
        self.destination_logic.update_information_destination(line, column, update)

    def add_crew_to_voyage(self, line, column, update):
        self.voyage_logic.add_crew_voyage(line, column, update)

    def create_a_voyage(self, voyage):
        self.voyage_logic.create_voyage(voyage)

    def week_start_to_end(self, year, month, day):
        return self.schedules_logic.weekly_period(year, month, day)

    def send_employee_schedule(self, name, start, end):
        return self.schedules_logic.check_employee_period(name, start, end)
