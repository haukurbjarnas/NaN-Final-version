from data.data_wrapper import DataWrapper

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