from logic.logic_wrapper import LogicWrapper
import datetime

class SchedulesUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def schedule_menu(self):
        print("Employee Schedules")
        print("1. See employee specific weekly schedule")
        print("2. Check which employees are available by day")
        print("3. Check which employees are working and to what destination they are assigned")
        


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

        employee = all_employees[int(select_employee)-1].name

        start_input = input("Enter start of weekly period (YYYY MM DD): ")

        year, month, day = start_input.split()

        start, end = self.logic_wrapper.week_start_to_end(int(year), int(month), int(day))

        the_schedule = self.logic_wrapper.send_employee_schedule(employee, start, end)

        for voyage in the_schedule:
            print(voyage.number_id)


    def are_employees_working_that_day(self):

        pass