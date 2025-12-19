def show_students(students):
    print("\n--- Student List ---")
    for s in students:
        s.show()

def show_courses(courses):
    print("\n--- Course List ---")
    for c in courses:
        c.show()

def show_marks(students, marks):
    cid = input("Enter course ID to see marks: ")
    if cid in marks:
        print(f"\nMarks for Course {cid}:")
        for sid, score in marks[cid]:
            name = next((s.name for s in students if s.sid == sid), "Unknown")
            print(f"{sid} - {name}: {score}")
    else:
        print("No marks found for this course.")