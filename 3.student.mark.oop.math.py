class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 55:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))
        print("Grade:", self.grade())


student_id = input("Enter student ID: ")
name = input("Enter student name: ")

marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

student = Student(student_id, name, marks)
student.display()
