class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Roll No    : {self.roll_no}")
        print(f"Name       : {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Percentage : {self.percentage():.2f}%")
        print("-" * 30)


s1 = Student(1, "Aarav", [85, 90, 78, 92, 88])
s2 = Student(2, "Diya", [70, 65, 80, 75, 72])
s3 = Student(3, "Kabir", [95, 98, 91, 89, 94])

for s in (s1, s2, s3):
    s.display()
