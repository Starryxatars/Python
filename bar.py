
import matplotlib.pyplot as plt

students = ["Rehan", "Arshad", "Varad", "Shiva", "Rohit"]
marks = [70, 85, 90, 65, 80]

plt.bar(students, marks)

plt.title("Student Marks - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
