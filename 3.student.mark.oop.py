import math
import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.scores = []  

    def add_score(self, score):
    
        score = math.floor(score * 10) / 10
        self.scores.append(score)

    def average(self):
        if len(self.scores) == 0:
            return 0.0
        return float(np.mean(self.scores))

    def show(self):
        print(
            self.sid, "-", self.name,
            "DoB:", self.dob,
            "| Avg:", f"{self.average():.2f}"
        )

class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def show(self):
        print(self.cid, "-", self.name)


students = []
courses = []
marks = {}  

num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print("Student", i + 1)
    sid = input("ID: ")
    name = input("Name: ")
    dob = input("DoB: ")
    students.append(Student(sid, name, dob))

num_courses = int(input("\nEnter number of courses: "))
for i in range(num_courses):
    print("Course", i + 1)
    cid = input("ID: ")
    cname = input("Name: ")
    courses.append(Course(cid, cname))

print("\nSelect course to input marks:")
for c in courses:
    c.show()

course_id = input("Enter course ID: ")
marks[course_id] = []

print("Enter marks for each student:")
for s in students:
    score = float(input(f"Mark for {s.name}: "))
    score = math.floor(score * 10) / 10
    marks[course_id].append((s.sid, score))
    s.add_score(score)

while True:
    print("\nMenu:")
    print("1. List students")
    print("2. List courses")
    print("3. Show marks for course")
    print("4. Sort students by average mark")
    print("0. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("\nStudents:")
        for s in students:
            s.show()

    elif choice == "2":
        print("\nCourses:")
        for c in courses:
            c.show()

    elif choice == "3":
        cid = input("Enter course ID: ")
        if cid in marks:
            print("Marks for course", cid)
            for sid, score in marks[cid]:
                for s in students:
                    if s.sid == sid:
                        print(sid, "-", s.name, ":", score)
        else:
            print("No marks for this course.")

    elif choice == "4":
        students.sort(key=lambda s: s.average(), reverse=True)
        print("\nStudents sorted by average mark:")
        for s in students:
            s.show()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

