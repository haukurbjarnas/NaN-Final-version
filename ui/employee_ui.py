from logic.logic_wrapper import LogicWrapper
from models.crew import Crew

class EmployeeUI:
    
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def employee_menu(self):
        print("-"*50)
        print("Employee Management")
        print("1. Create employee")
        print("2. List pilots")
        print("3. List flight attendants")
        print("4. List all employees")
        print("5. Update employee")
        print("Enter (B)ack to go back")
        print("-"*50)
        print("")

    def input_prompt(self):
        while True:
            self.employee_menu()
            command = input("Enter a command: ")
            command = command.lower()
            if command == "1":
                self.create_employee()
            elif command == "2":
                self.print_pilots()
            elif command == "3":
                self.print_attendants()
            elif command == "4":
                self.print_all_employees()
            elif command == "5":
                self.update_employee()
            elif command == "b":
                return "b"
            else:
                print("Invalid input, try again")


    def create_employee(self):
        
        nid = self.logic_wrapper.get_lines_employees()
            
        while True:
            name = input("Enter name: ")
            if all(x.isalpha() or x.isspace() for x in name):
                break
            else:
                print("Invalid input try again..")
        
        while True:
            ssn = input("Enter social security number: ")
            if ssn.isdigit():
                break
            else:
                print("Invalid input try again..")
        
        while True:
            role_choice = input(f"Is (P)ILOT or (F)LIGHT ATTENDANT?: ")
            role_choice = role_choice.lower()
            if role_choice == "p" or role_choice == "pilot":
                role = "Pilot"
                break
            elif role_choice == "f" or role_choice == "flight attendant" or role_choice == "flightattendant":
                role = "Flight attendant"
                break
            else:
                print("Invalid input try again..")

        while True:
            if role == "Pilot":
                print(f"What role does {name} have as a {role}? 1. Captain or 2. Co-Pilot")
                try:
                    rank_choice = int(input("Select either option 1. or 2.: "))
                except ValueError:
                    print("Please input the number associated with the rank")
                if rank_choice == 1:
                    rank = "Captain"
                    break
                elif rank_choice == 2:
                    rank = "Co-Pilot"
                    break
            if role == "Flight attendant":
                print(f"What role does {name} have as a {role}? 1. Main flight attendant or 2. Normal Flight attendant")
                try:
                    rank_choice = int(input("Select either option 1. or 2.: "))
                except ValueError:
                    print("Please input the number associated with the rank")
                if rank_choice == 1:
                    rank = "Main flight attendant"
                    break
                elif rank_choice == 2:
                    rank = "Normal Flight attendant"
                    break
                else:
                    print("Invalid input try again..")


        while True:
            phone = input("Enter phone number: ")
            if phone.isdigit():
                break
            else:
                print("Invalid input try again..")

        while True:
            email = input("Enter e-mail address: ")
            if email.isascii() and 0 < len(email) < 40:
                break
            else:
                print("Invalid input try again..")

        while True:
            address = input("Enter home address (street and number): ")
            if all(x.isalnum() or x.isspace() for x in address):
                break
            else:
                print("Invalid input try again..")

        while True:
            home_phone = input("Enter home phone number (optional) press enter if you do not wish to add home phone number: ")
            if home_phone.isdigit() or home_phone == "":
                break
            else:
                print("Invalid input try again..")

        employee = Crew(nid, name, ssn, role, rank, phone, email, address, home_phone)
        
        self.logic_wrapper.add_employee(employee)

        print("Employee created successfully!")

    def print_all_employees(self):
        
        result = self.logic_wrapper.list_all_employees()
        for elem in result:
            print("-"*50)
            print(f"Number ID: {elem.nid}")
            print(f"Name: {elem.name}")
            print(f"SSN: {elem.ssn}")
            print(f"Role: {elem.rank}")
            print(f"Rank: {elem.role}")
            print(f"Phone number: {elem.phone_nr}")
            print(f"e-Mail: {elem.email}")
            print(f"Address: {elem.address}")
            print(f"Home phone number: {elem.home_phone}")
            print("-"*50)
            print("")

    def print_pilots(self):
        print("-"*40)
        a_list = self.logic_wrapper.list_all_pilots()

        for pilot in a_list:
            print(f"Name: {pilot.name}, Rank: {pilot.rank}")
        print("-"*40)
    def print_attendants(self):
        print("-"*40)
        a_list = self.logic_wrapper.list_all_attendants()

        for attendant in a_list:
            print(f"Name: {attendant.name}, Rank: {attendant.rank}")
        print("-"*40)
    def update_employee(self):
        
        all_employees = self.logic_wrapper.list_all_employees()

        num = 1
        print("-"*40)
        for full_name in all_employees:
            print(f"{num}. {full_name.name}")
            num += 1
        print("-"*40)
        while True:
            name_of = (input("Select an employee: "))
            if name_of.isdigit() and 0 < int(name_of) <num:
                break
            else:
                print("Invalid input try again..")
        
        print("-"*50)    
        print("Select what you want to update: ")
        print("1. Phone number")
        print("2. E-Mail")
        print("3. Address")
        print("4. Home phone number")
        print("-"*50)
        print("")

        

        while True:
            what_to_update = input("Select what you want to update: ")
            update = ""

            if what_to_update == "1":
                update = "phone_nr"
            elif what_to_update == "2":
                update = "email"
            elif what_to_update == "3":
                update = "address"
            elif what_to_update == "4":
                update = "home_phone"
            else:
                print("Invalid input try again..")
                continue  

            while True:
                new_info = input(f"Enter new info: ")

                if (update == "phone_nr" or update == "home_phone") and new_info.isdigit() and len(new_info) <= 10:
                    break
                elif update == "email" and new_info.isascii() and len(new_info) <= 40:
                    break
                elif update == "address" and all(x.isascii() or x.isspace() for x in new_info):
                    break
                else:
                    print("Invalid input try again..")

            
            break



        self.logic_wrapper.new_information_employee(int(name_of)-1, update, new_info)

        print("Update successful...")