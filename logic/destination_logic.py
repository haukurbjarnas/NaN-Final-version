from data.data_wrapper import DataWrapper
class DestinationLogic:
    
    def __init__(self):
        self.data_wrapper = DataWrapper()

    def add_destination(self, destination):
        self.data_wrapper.create_destination(destination)

    def get_all_destinations(self):
        return self.data_wrapper.read_all_destinations()
    
    def update_information_destination(self, line, column, update):
        self.data_wrapper.update_destination(line, column, update)

    def count_lines_in_csv(self):
        return self.data_wrapper.get_lines_destinations()