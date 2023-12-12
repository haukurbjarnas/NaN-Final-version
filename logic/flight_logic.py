from data.data_wrapper import DataWrapper 

class FlightLogic: 

    def __init__(self):
        self.flight_wrapper = DataWrapper() 

    def add_flight(self, flight): 
        '''Adds a flight to the data base'''
        self.flight_wrapper.create_flight(flight)  
       
        if self.flight_wrapper.get_flight_by_flight_number(flight.flight_number) != None: 
            return error_1 
        
        else :
            return successful

    def get_all_flights(self): 
        return self.flight_wrapper.read_all_flights() 

    def update_information_flight(self, line, column, update):
        self.flight_wrapper.update_flight(line, column, update)

