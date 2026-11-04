class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        return self.basic


class Manager(Employee):
    def calculate_salary(self):

        return self.basic + 0.40 * self.basic + 0.20 * self.basic


class Developer(Employee):
    def calculate_salary(self):

        return self.basic + 0.30 * self.basic + 0.15 * self.basic


class Tester(Employee):
    def calculate_salary(self):

        return self.basic + 0.25 * self.basic + 0.10 * self.basic


staff = [Manager("Anjali", 60000), Developer("Rohan", 50000), Tester("Meera", 40000)]
for e in staff:
    print(f"{e.__class__.__name__:<10} {e.name:<8} Salary: Rs. {e.calculate_salary():.2f}")
