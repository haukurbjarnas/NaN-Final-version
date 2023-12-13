from data.data_wrapper import DataWrapper 

class VoyageLogic: 

    def __init__(self):
        self.voyage_wrapper = DataWrapper() 

    def add_voyage(self, voyage): 
        '''Adds a voyage to the data base'''
        voyage_error_1 = 1 
        voyage_error_2 = 2 
        #voyage_error_3 = 3 
        voyage_successful = 0 

        if self.voyage_wrapper.get_voyage_by_flight_nr(voyage.flight_nr) != None: 
            return voyage_error_1
        
        elif self.voyage_wrapper.get_voyage_by_flight_nr_back(voyage.flight_nr_back) != None: 
            return voyage_error_2 
        else:
            self.voyage_wrapper.create_voyage(voyage) 
            return voyage_successful

    def get_all_voyages(self): 
        return self.voyage_wrapper.read_all_voyages() 

    