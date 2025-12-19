import os
import zipfile
import pickle
import threading
from domains.student import Student
from domains.course import Course
from input import input_students, input_courses, input_marks
from output import show_students, show_courses, show_marks

def background_save(students, courses, marks):
    data = {'s': students, 'c': courses, 'm': marks}
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    with zipfile.ZipFile("students.dat", "w") as zipf:
        zipf.write("data.pkl")
    if os.path.exists("data.pkl"):
        os.remove("data.pkl")
    print("\n[System] Background save complete.")

def save_data(students, courses, marks):
    save_thread = threading.Thread(target=background_save, args=(students, courses, marks))
    save_thread.start()
    save_thread.join()

def load_data():
    students, courses, marks = [], [], {}
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()
        if os.path.exists("data.pkl"):
            with open("data.pkl", "rb") as f:
                data = pickle.load(f)
                students = data.get('s', [])
                courses = data.get('c', [])
                marks = data.get('m', {})
            os.remove("data.pkl")
    return students, courses, marks

def main():
    students, courses, marks = load_data()
    while True:
        print("\n--- Student Management (PW8) ---")
        print("1. Show Students")
        print("2. Show Courses")
        print("3. Show Marks")
        print("4. Add Students")
        print("5. Add Courses")
        print("6. Input Marks")
        print("0. Exit")
        choice = input("Your choice: ")
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
            save_data(students, courses, marks)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()