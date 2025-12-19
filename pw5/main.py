import zipfile
import os
from domains.student import Student
from domains.course import Course
from input import input_students, input_courses, input_marks
from output import show_students, show_courses, show_marks


def compress_data():
    """Bundles txt files into students.dat and cleans up."""
    files = ["students.txt", "courses.txt", "marks.txt"]
    with zipfile.ZipFile("students.dat", "w") as zipf:
        for file in files:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file) 
    print("\nData compressed and saved to students.dat")

def load_data():
    """Extracts students.dat and converts text back into Python objects."""
    students = []
    courses = []
    marks = {}

    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()
        
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        students.append(Student(parts[0], parts[1], parts[2]))
        
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        courses.append(Course(parts[0], parts[1]))
        
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r") as f:
                for line in f:
                    cid, sid, score = line.strip().split(',')
                    if cid not in marks: marks[cid] = []
                    marks[cid].append((sid, float(score)))
        
        print("Data loaded successfully from previous session.")
    return students, courses, marks


def main():
   
    students, courses, marks = load_data()

    while True:
        print("\n--- MENU ---")
        print("1. List students")
        print("2. List courses")
        print("3. Show marks")
        print("4. Add students")
        print("5. Add courses")
        print("6. Input marks")
        print("0. Exit and Save")

        choice = input("Select: ")

        if choice == "1":
            show_students(students)
        elif choice == "2":
            show_courses(courses)
        elif choice == "3":
            show_marks(students, marks)
        elif choice == "4":
            students.extend(input_students())
        elif choice == "5":
            courses.extend(input_courses())
        elif choice == "6":
            new_marks = input_marks(students, courses)
            marks.update(new_marks)
        elif choice == "0":
            compress_data()
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()