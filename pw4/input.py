from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("Student", i + 1)
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append(Student(sid, name, dob))
    return students

def input_courses():
    courses = []
    n = int(input("\nEnter number of courses: "))
    for i in range(n):
        print("Course", i + 1)
        cid = input("ID: ")
        name = input("Name: ")
        courses.append(Course(cid, name))
    return courses

def input_marks(students, courses):
    marks = {}
    print("\nSelect course to input marks:")
    for c in courses:
        c.show()

    cid = input("Enter course ID: ")
    marks[cid] = []

    for s in students:
        score = float(input(f"Mark for {s.name}: "))
        s.add_score(score)
        marks[cid].append((s.sid, score))

    return marks
