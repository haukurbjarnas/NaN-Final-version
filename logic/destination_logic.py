from data.data_wrapper import DataWrapper

class DestinationLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def add_destination(self, destination): 

        destination_error_1 = 1 
        destination_error_2 = 2 
        destination_successful = 3

        if self.data_wrapper.get_destination_by_id(destination.destination_id) != None: 
            return destination_error_1 
        
        elif self.data_wrapper.get_destination_by_numeric_id(destination.numeric_id) != None: 
            return destination_error_2 
        
        else:
            self.data_wrapper.create_destination(destination) 
            return destination_successful


    def get_all_destinations(self):
        return self.data_wrapper.read_all_destinations()