from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    try:
        n = int(input("Enter number of students: "))
        for i in range(n):
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            students.append(Student(sid, name, dob))
    except ValueError:
        pass
    return students

def input_courses():
    courses = []
    try:
        n = int(input("Enter number of courses: "))
        for i in range(n):
            cid = input("ID: ")
            name = input("Name: ")
            courses.append(Course(cid, name))
    except ValueError:
        pass
    return courses

def input_marks(students, courses):
    marks = {}
    if not courses:
        return marks
    for c in courses:
        c.show()
    cid = input("Enter course ID: ")
    marks[cid] = []
    for s in students:
        try:
            score = float(input(f"Mark for {s.name}: "))
            marks[cid].append((s.sid, score))
        except ValueError:
            pass
    return marks