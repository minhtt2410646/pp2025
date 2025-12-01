num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print("Student", i+1)
    sid = input("ID: ")
    name = input("Name: ")
    dob = input("DoB: ")
    students.append((sid, name, dob))

num_courses = int(input("\nEnter number of courses: "))
for i in range(num_courses):
    print("Course", i+1)
    cid = input("ID: ")
    cname = input("Name: ")
    courses.append((cid, cname))

print("\nSelect course to input marks:")
for c in courses:
    print(c[0], "-", c[1])

course_id = input("Enter course ID: ")
marks[course_id] = []

print("Enter marks for each student:")
for s in students:
    sid, name, dob = s
    score = float(input(f"Mark for {name}: "))
    marks[course_id].append((sid, score))

while True:
    print("\nMenu:")
    print("1. List students")
    print("2. List courses")
    print("3. Show marks for course")
    print("0. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print("\nStudents:")
        for s in students:
            print(s[0], "-", s[1], "DoB:", s[2])
    elif choice == "2":
        print("\nCourses:")
        for c in courses:
            print(c[0], "-", c[1])
    elif choice == "3":
        cid = input("Enter course ID: ")
        if cid in marks:
            print("Marks for course", cid)
            for sid, score in marks[cid]:
                name = next(s[1] for s in students if s[0] == sid)
                print(sid, "-", name, ":", score)
        else:
            print("No marks for this course.")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

