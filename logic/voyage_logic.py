from data.data_wrapper import DataWrapper
import datetime
import csv

class VoyageLogic:

    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

    def connected_flights(self, flight):

        matching_list = []

        all_flights = self.data_wrapper.read_all_flights()

        flight_one_departure = flight.dep_from
        flight_one_arrival = flight.arr_at

        for elem in all_flights:
            if flight_one_departure == elem.arr_at and flight_one_arrival == elem.dep_from:
                matching_list.append(elem)

        return matching_list
    
    def get_all_voyages(self):
        return self.data_wrapper.read_add_voyages()
    
    def add_crew_voyage(self, line, column, update):
        self.data_wrapper.add_crew_to_voyage(line, column, update)

    def create_voyage(self, voyage):
        self.data_wrapper.create_voyage(voyage)

    def count_lines_in_csv(self):
        return self.data_wrapper.get_lines_voyages()
    
    def understaffed_voyages(self):

        all_voyages = self.data_wrapper.read_add_voyages()

        understaffed_voyage_list = []


        for voyage in all_voyages:

            if voyage.captain == None:
                understaffed_voyage_list.append(voyage)
            
            elif voyage.copilot == None:
                understaffed_voyage_list.append(voyage)

            elif voyage.fa1 == None:
                understaffed_voyage_list.append(voyage)

            elif voyage.fa2 == None:
                understaffed_voyage_list.append(voyage)

        return understaffed_voyage_list

    def staffed_voyages(self):

        all_voyages = self.data_wrapper.read_add_voyages()

        staffed_voyage_list = []


        for voyage in all_voyages:

            if voyage.captain and voyage.copilot and voyage.fa1 and voyage.fa2:
                staffed_voyage_list.append(voyage)
            

        return staffed_voyage_list
    


    def weekly_period(self, year, month, day):
        '''Receives start of a weekly period and returns the end of the weekly period to UI layer'''
        
        start_of_period = datetime.date(year, month, day)

        period = datetime.timedelta(days = 7)

        end_of_period = start_of_period + period

        return start_of_period, end_of_period
    
    def check_crew_in_voyage_by_week(self, start):

        year, month, day = start.split()
        
        start_period, end_period = self.weekly_period(int(year), int(month), int(day))
        
        all_voyages = self.data_wrapper.read_add_voyages()
        all_flights = self.data_wrapper.read_all_flights()

        period_voyage = []

        for voyage in all_voyages:
            for flight in all_flights:
                if voyage.flight_nr == flight.flight_nr or voyage.flight_nr_back == flight.flight_nr:
                    year1, month1, day1 = flight.departure_time.split()
                    year2, month2, day2 = flight.arrival_time.split()
                    time1 = datetime.date(int(year1), int(month1), int(day1))
                    time2 = datetime.date(int(year2), int(month2), int(day2))
                    if (start_period < time1) and (end_period > time1) and (start_period < time2) and (end_period > time2):
                        period_voyage.append(voyage)

        return period_voyage


    def check_crew_in_voyage_by_day(self, theday):

        all_voyages = self.data_wrapper.read_add_voyages()
        all_flights = self.data_wrapper.read_all_flights()
        
        year, month, day = theday.split()

        formatted_day = datetime.date(int(year), int(month), int(day))

        day_voyages = []

        for voyage in all_voyages:
            for flight in all_flights:
                if voyage.flight_nr == flight.flight_nr or voyage.flight_nr_back == flight.flight_nr:
                    year1, month1, day1 = flight.departure_time.split()
                    year2, month2, day2 = flight.arrival_time.split()
                    time1 = datetime.date(int(year1), int(month1), int(day1))
                    time2 = datetime.date(int(year2), int(month2), int(day2))
                    if (formatted_day == time1) and (formatted_day == time2):
                        day_voyages.append(voyage)

        return day_voyages
    

    
    def check_matching_day(self, voyage_to_check, name):

        a_list = []

        all_voyages = self.data_wrapper.read_add_voyages()
        all_flights = self.data_wrapper.read_all_flights()

        for voyage in all_voyages:
            if voyage == voyage_to_check:
                pass
            else:
                if voyage.captain == name or voyage.copilot == name or voyage.fa1 == name or voyage.fa2 == name:
                    if voyage.date1 == voyage_to_check.date1 or voyage.date1 == voyage_to_check.date2 or voyage.date2 == voyage_to_check.date1 or voyage.date2 == voyage_to_check.date2:
                        a_list.append(1)

        return a_list


        
