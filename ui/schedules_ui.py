from logic.logic_wrapper import LogicWrapper

class SchedulesUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def schedule_menu(self):
        print("Employee Schedules")
        print("1. See employee specific weekly schedule")
        print("2. Available employees")
        print("3. Working employees")