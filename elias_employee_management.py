
FILE_NAME = "employee.txt"

def add_employee(name, employee_id, salary):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {employee_id} | {salary}\n")

    return True

def view_employee():
    try:
        with open(FILE_NAME, "r") as file:
            employee = file.readlines()

        return employee

    except FileNotFoundError:
        return []

def display_employees():
    employee = view_employee()

    if not employee:
        print("No employee records found.")
        return

    print("\nEmployee Records")

    for employee in employee:
        print(employee.strip())

def main():
    while True:
        print("\nEmployee Salary Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            employee_id = input("Enter ID: ")

            try:
                salary = float(input("Enter Salary: "))

                if salary < 0:
                    print("Salary cannot be negative.")
                    continue

            except ValueError:
                print("Invalid salary. Please enter a number.")
                continue

            add_employee(name, employee_id, salary)

            print("Employee Added Successfully")

        elif choice == "2":
            display_employees()

        elif choice == "3":
            print("Thank you for using the system")
            break

        else:
            print("Invalid")

if __name__ == "__main__":
    main()