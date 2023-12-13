from data.data_wrapper import DataWrapper

class DestinationLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def add_destination(self, destination): 

        if self.data_wrapper.get_destination_by_id(destination.id) is not None:
            raise ValueError("A destination with this ID already exists.")

        if self.data_wrapper.get_destination_by_numericid(destination.numeric_id) is not None: 
            raise ValueError("A destination with this numeric ID already exists.")

        if self.data_wrapper.get_destination_by_airport(destination.airport) is not None: 
            raise ValueError("A destination with this airport already exists.")

        self.data_wrapper.create_destination(destination)

    def get_all_destinations(self):
        return self.data_wrapper.read_all_destinations() 
    
    def update_information_destination(self, line, column, update): 
        self.data_wrapper.update_destination(line, column, update) 

    def get_destination_by_id(self, id): 
        return self.data_wrapper.get_destination_by_id(id) 

        


