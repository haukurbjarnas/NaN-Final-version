import datetime
from data.data_wrapper import DataWrapper

class SchedulesLogic:

    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()

    def weekly_period(self, year, month, day):
        '''Receives start of a weekly period and returns the end of the weekly period to UI layer'''
        
        start_of_period = datetime.date(year, month, day)

        period = datetime.timedelta(days = 7)

        end_of_period = start_of_period + period

        return start_of_period, end_of_period
    
    def check_employee_period(self, name, start, end):
        '''Checks if any dates within the period is found within flights assigned to crew member'''

        all_voyages = self.data_wrapper.read_add_voyages()

        all_flights = self.data_wrapper.read_all_flights()

        matching_voyage = []

        
        for voyage in all_voyages:
            if name == voyage.captain or name == voyage.copilot or name == voyage.fa1 or name == voyage.fa2:
                for flight in all_flights:
                    if voyage.flight_nr == flight.flight_nr or voyage.flight_nr_back == flight.flight_nr:
                        year1, month1, day1 = flight.departure_time.split()
                        year2, month2, day2 = flight.arrival_time.split()
                        time1 = datetime.date(int(year1), int(month1), int(day1))
                        time2 = datetime.date(int(year2), int(month2), int(day2))
                        if (start <= time1) and (end >= time1) and (start <= time2) and (end >= time2):
                            matching_voyage.append(voyage)
                            break

       
        return matching_voyage
    
