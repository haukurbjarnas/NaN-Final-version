from models.voyage import Voyage
from logic.logic_wrapper import LogicWrapper

class VoyageUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def voyage_menu(self):
        print("Voyage Management")
        print("1. Create voyage")
        print("2. List all voyages")
    
    def input_prompt(self):
        pass

    def create_a_voyage(self):

        pass