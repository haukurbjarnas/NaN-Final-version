from data.data_wrapper import DataWrapper 

class VoyageLogic: 

    def __init__(self):
        self.voyage_wrapper = DataWrapper() 

    def add_voyage(self, voyage): 
        '''Adds a voyage to the data base'''
        self.voyage_wrapper.create_voyage(voyage) 

    def get_all_voyages(self): 
        return self.voyage_wrapper.read_all_voyages() 

    