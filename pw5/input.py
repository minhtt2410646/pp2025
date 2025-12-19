import os
from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    try:
        n = int(input("Enter number of students: "))
    except ValueError:
        return []

    with open("students.txt", "a") as f:
        for i in range(n):
            print(f"Student {i + 1}")
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            
            f.write(f"{sid},{name},{dob}\n")
            students.append(Student(sid, name, dob))
    return students

def input_courses():
    courses = []
    try:
        n = int(input("\nEnter number of courses: "))
    except ValueError:
        return []

    with open("courses.txt", "a") as f:
        for i in range(n):
            print(f"Course {i + 1}")
            cid = input("ID: ")
            name = input("Name: ")
            
            f.write(f"{cid},{name}\n")
            courses.append(Course(cid, name))
    return courses

def input_marks(students, courses):
    marks = {}
    if not courses:
        print("No courses available.")
        return marks
        
    print("\nSelect course to input marks:")
    for c in courses:
        c.show()
    
    cid = input("Enter course ID: ")
    marks[cid] = []

    with open("marks.txt", "a") as f:
        for s in students:
            try:
                score = float(input(f"Mark for {s.name}: "))
                
                s.add_score(score) 
                
                f.write(f"{cid},{s.sid},{score}\n")
                marks[cid].append((s.sid, score))
            except ValueError:
                print("Invalid score. Skipping.")
    return marks