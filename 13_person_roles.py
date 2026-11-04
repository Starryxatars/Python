class Person:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        print(f"{self.name} is a person.")


class Student(Person):
    def display_role(self):
        print(f"{self.name} is a Student: attends classes and writes exams.")


class Faculty(Person):
    def display_role(self):
        print(f"{self.name} is a Faculty member: teaches and guides students.")


class Administrator(Person):
    def display_role(self):
        print(f"{self.name} is an Administrator: manages college operations.")


people = [Student("Aarav"), Faculty("Dr. Mehta"), Administrator("Mr. Sharma")]

for person in people:
    person.display_role()
