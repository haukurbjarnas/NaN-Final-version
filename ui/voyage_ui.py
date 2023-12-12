from models.voyage import Voyage
from logic.logic_wrapper import LogicWrapper

class VoyageUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def voyage_menu(self):
        print("Voyage Management")
        print("1. Create voyage")
        print("2. List all voyages")
        print("3. Add crew to voyage")
    
    def input_prompt(self):
        while True:
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                pass
            if command == "2":
                pass
            if command == "3":
                pass
            else:
                print("Invalid input!")

    def create_a_voyage(self):

        pass

    def print_all_voyages(self):

        pass

    def add_crew_to_voyage(self):

        pass