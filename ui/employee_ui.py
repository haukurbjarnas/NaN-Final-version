from logic.logic_wrapper import LogicWrapper
from models.crew import Crew

class EmployeeUI:
    
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def employee_menu(self):
        print("")
        print("Employee Management")
        print("1. Create employee")
        print("2. List pilots")
        print("3. List flight attendants")
        print("4. List all employees")
        print("5. Update employee")
        print("Enter (B)ack to go back")

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
        while True:
            nid = input("Enter number ID for the employee: ")
            if nid.isdigit():
                break
            else:
                print("Invalid input!")
            
        while True:
            name = input("Enter name: ")
            if all(x.isalpha() or x.isspace() for x in name):
                break
            else:
                print("Invalid input!")
        
        while True:
            ssn = input("Enter social security number: ")
            if ssn.isdigit():
                break
            else:
                print("Invalid input!")
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
                print("Invalid input!")

        while True:
            rank = input("What is the rank? ")
            if rank.isalpha():
                break
            else: 
                print("Invalid input!")


        while True:
            phone = input("Enter phone number: ")
            if phone.isdigit() and len(phone) == 7:
                break
            else:
                print("Invalid input! Phone NUMBERS only include NUMBERS ;P")

        while True:
            email = input("Enter e-mail address: ")
            if len(email) < 40:
                break
            else:
                print("Invalid input!")

        while True:
            address = input("Enter home address (street and number): ")
            if all(x.isalnum() or x.isspace() for x in name):
                break
            else:
                print("Invalid input!")

    

        employee = Crew(nid, name, ssn, role, rank, phone, email, address)
        
        self.logic_wrapper.add_employee(employee)
        print("Employee created succesfully!")
        
    def print_all_employees(self):
        
        result = self.logic_wrapper.list_all_employees()
        print("All EMPLOYEES:")
        for elem in result:
            print("")
            print("-"*30)
            print(f"Number ID: {elem.nid}")
            print(f"Name: {elem.name}")
            print(f"SSN: {elem.ssn}")
            print(f"Role: {elem.rank}")
            print(f"Rank: {elem.role}")
            print(f"Phone number: {elem.phone_nr}")
            print(f"e-Mail: {elem.email}")
            print(f"Address: {elem.address}")
            print("-"*30)
            print("")

    def print_pilots(self):
        
        a_list = self.logic_wrapper.list_all_pilots()

        for elem in a_list:
            print("-"*40)
            print(elem)
            
        print("-"*40)
    def print_attendants(self):
        a_list = self.logic_wrapper.list_all_attendants()

        for elem in a_list:
            print("-"*40)
            print(elem)
        print("-"*40)

    def update_employee(self):
        
        all_employees = self.logic_wrapper.list_all_employees()

        num = 1

        for full_name in all_employees:
            print(f"{num}. {full_name.name}")
            num += 1

        while True:
            name_of = input("Select an employee: ")
            if name_of.isdigit():
                break
            else:
                print("Invalid input!")
            
        print("Select what you want to update: ")
        print("1. Role")
        print("2. Rank")
        print("3. Phone number")
        print("4. E-Mail")
        print("5. Address")

        what_to_update = input("Select what you want to update: ")

        while True:
            if what_to_update == "1":
                update = "role"
                break
            elif what_to_update == "2":
                update = "rank"
                break
            elif what_to_update == "3":
                update = "phone_nr"
                break
            elif what_to_update == "4":
                update = "email"
                break
            elif what_to_update == "5":
                update = "address"
                break
            else:
                print("Invalid input!")

        new_info = input("Enter new info: ")

        self.logic_wrapper.new_information_employee(int(name_of)-1, update, new_info)
        print("Update successful...")
        