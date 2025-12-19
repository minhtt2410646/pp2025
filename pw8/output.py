def show_students(students):
    for s in students:
        s.show()

def show_courses(courses):
    for c in courses:
        c.show()

def show_marks(students, marks):
    cid = input("Enter course ID: ")
    if cid in marks:
        for sid, score in marks[cid]:
            name = next((s.name for s in students if s.sid == sid), "Unknown")
            print(f"{name}: {score}")