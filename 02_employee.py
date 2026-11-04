class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.basic_salary

    def calculate_da(self):
        return 0.50 * self.basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print(f"Employee ID  : {self.emp_id}")
        print(f"Name         : {self.name}")
        print(f"Basic Salary : {self.basic_salary:.2f}")
        print(f"HRA (20%)    : {self.calculate_hra():.2f}")
        print(f"DA (50%)     : {self.calculate_da():.2f}")
        print(f"Gross Salary : {self.calculate_gross_salary():.2f}")


emp_id = int(input("Enter employee ID: "))
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

emp = Employee(emp_id, name, basic)
print()
emp.display()
