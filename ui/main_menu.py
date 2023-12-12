from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from ui.destination_ui import DestinationUI

class MainMenu:

    def __init__(self):
        pass
    
    def menu_output(self):
        print("")
        print("Main Menu - Welcome!")
        print("1. Employee management")
        print("2. Voyage management")
        print("3. Flight managemnt")
        print("4. Destination management")
        print("5. Employee schedules")
        print("(Q)uit to exit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye...")
                exit()
            elif command == "1":
                menu = EmployeeUI()
                back = menu.input_prompt()
                if back == "q":
                    return "q"
            elif command == "2":
                menu = VoyageUI()
                back = menu.input_prompt()
                if back == "q":
                    return "q"
            elif command == "3":
                pass
            elif command == "4":
                menu = DestinationUI()
                back = menu.input_prompt()
                if back == "q":
                    return "q"
            elif command == "5":
                pass
            else:
                print("Invalid input!")
