from logic.logic_wrapper import LogicWrapper

class SchedulesUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def schedule_menu(self):
        print("Employee Schedules")
        print("1. See employee specific weekly schedule")
        print("2. Available employees")
        print("3. Working employees")

    def input_prompt(self):
        while True:
            self.schedule_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.employee_specific_schedule()
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "b":
                return "b"
            else:
                print("Invalid input!")

    def employee_specific_schedule(self):

        all_employees = self.logic_wrapper.list_all_employees()

        num = 1
        for elem in all_employees:
            print(f"{num}. Name: {elem.name} Role: {elem.role}")
            num += 1

        select_employee = int(input("Select an employee: "))

        employee = all_employees[select_employee-1].name

        print(employee)