class Student:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def calculate_grade(self):
        return "Not defined"


class EngineeringStudent(Student):
    def calculate_grade(self):
        p = self.percentage
        if p >= 85:
            return "Distinction"
        elif p >= 60:
            return "First Class"
        elif p >= 50:
            return "Second Class"
        elif p >= 40:
            return "Pass"
        return "Fail"


class MedicalStudent(Student):
    def calculate_grade(self):

        p = self.percentage
        if p >= 90:
            return "A (Honours)"
        elif p >= 75:
            return "B"
        elif p >= 50:
            return "C"
        return "Fail"


class ManagementStudent(Student):
    def calculate_grade(self):

        p = self.percentage
        if p >= 80:
            return "A+"
        elif p >= 70:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 45:
            return "C"
        return "Fail"


students = [EngineeringStudent("Aarav", 78),
            MedicalStudent("Diya", 78),
            ManagementStudent("Kabir", 78)]

for s in students:
    print(f"{s.__class__.__name__:<20} {s.name:<6} {s.percentage}% -> {s.calculate_grade()}")
