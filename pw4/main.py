from input import input_students, input_courses, input_marks
from output import show_students, show_courses, show_marks

def main():
    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Show marks for course")
        print("4. Sort students by average mark")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            show_students(students)
        elif choice == "2":
            show_courses(courses)
        elif choice == "3":
            show_marks(students, marks)
        elif choice == "4":
            students.sort(key=lambda s: s.average(), reverse=True)
            show_students(students)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
