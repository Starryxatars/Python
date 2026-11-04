class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"Result record created for {self.name}.")

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        p = self.calculate_percentage()
        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"\nStudent Name : {self.name}")
        print(f"Marks        : {self.marks}")
        print(f"Total        : {self.calculate_total()} / {len(self.marks) * 100}")
        print(f"Percentage   : {self.calculate_percentage():.2f}%")
        print(f"Grade        : {self.calculate_grade()}")

    def __del__(self):
        print(f"\nResult record of {self.name} is being deleted.")


name = input("Enter student name: ")
marks = [int(input(f"Enter marks in subject {i} (out of 100): ")) for i in range(1, 6)]

result = StudentResult(name, marks)
result.display()
del result
