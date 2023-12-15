from logic.logic_wrapper import LogicWrapper
import datetime

class SchedulesUI:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def schedule_menu(self):
        print("-"*50)
        print("Employee Schedules")
        print("1. See employee specific weekly schedule")
        print("2. Check which employees are available by day")
        print("3. Check which employees are working and to what destination they are assigned")
        print("Enter (B)ack to go back")
        print("-"*50)
        print("")

    def input_prompt(self):
        while True:
            self.schedule_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.employee_specific_schedule()
            elif command == "2":
                self.employees_not_working_that_day()
            elif command == "3":
                self.are_employees_working_that_day()
            elif command == "b":
                return "b"
            else:
                print("Invalid input try again..")

    def employee_specific_schedule(self):
        all_employees = self.logic_wrapper.list_all_employees()

        if not all_employees:
            print("No employees found.")
            return

        num = 1
        for elem in all_employees:
            print(f"{num}. Name: {elem.name} Role: {elem.role}")
            num += 1

        try:
            select_employee = int(input("Select an employee: "))
            if select_employee < 1 or select_employee > len(all_employees):
                print("Invalid input try again..")
                return
        except ValueError:
            print("Invalid input try again..")
            return

        employee = all_employees[select_employee - 1].name

        try:
            start_input = input("Enter start of weekly period (YYYY MM DD): ")
            year, month, day = map(int, start_input.split())
            start, end = self.logic_wrapper.week_start_to_end(year, month, day)
        except (ValueError, IndexError):
            print("Invalid input try again..")
            return

        the_schedule = self.logic_wrapper.send_employee_schedule(employee, start, end)

        if not the_schedule:
            print("No schedule found for the selected employee.")
            return

        print("")
        print(f"WEEK SCHEDULE FOR {employee} FOR STARTING DATE {start_input}")
        for voyage in the_schedule:
            print(f"{voyage.date1} is {employee} assigned to voyage: {voyage.number_id}")

        print("-"*50)

    def are_employees_working_that_day(self):

        date = input("Enter date to check working employees: ")

        busy_employees = self.logic_wrapper.busy_employees(date)
        if not busy_employees:
            print("-"*50)
            print(f"No employees working {date}")
        for key in busy_employees.keys():
            print(f"{key}: going to {busy_employees[key]}")

    def employees_not_working_that_day(self):

        date = input("Enter date to check available employees: ")

        available_crew = self.logic_wrapper.available_employees(date)
        if not available_crew:
            print(f"No available crew members for {date}")
            return
        print("")
        print(f"ALL AVAILABLE EMPLOYEES {date}:")
        print("-"*50)
        for crew_member in available_crew:
            if crew_member == "":
                pass
            else:
                print(crew_member)
        
        