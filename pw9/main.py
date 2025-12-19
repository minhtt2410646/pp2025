import tkinter as tk
from tkinter import messagebox
import threading
import pickle
import zipfile
import os
from domains.student import Student
from domains.course import Course

def background_save(students, courses, marks):
    data = {'s': students, 'c': courses, 'm': marks}
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    with zipfile.ZipFile("students.dat", "w") as zipf:
        zipf.write("data.pkl")
    if os.path.exists("data.pkl"):
        os.remove("data.pkl")

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

class ManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System (PW9)")
        self.root.geometry("600x500")
        
        self.students, self.courses, self.marks = load_data()

        tk.Label(root, text="Management System", font=("Arial", 14, "bold")).pack(pady=10)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="List Students", width=15, command=self.list_s).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="List Courses", width=15, command=self.list_c).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Add Student", width=15, command=self.add_s_win).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Save & Exit", width=15, bg="red", fg="white", command=self.exit_app).grid(row=1, column=1, padx=5, pady=5)

        self.txt = tk.Text(root, height=15, width=70)
        self.txt.pack(pady=10)

    def list_s(self):
        self.txt.delete(1.0, tk.END)
        for s in self.students:
            self.txt.insert(tk.END, f"ID: {s.sid} | Name: {s.name}\n")

    def list_c(self):
        self.txt.delete(1.0, tk.END)
        for c in self.courses:
            self.txt.insert(tk.END, f"ID: {c.cid} | Name: {c.name}\n")

    def add_s_win(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="ID").pack()
        e1 = tk.Entry(win)
        e1.pack()
        tk.Label(win, text="Name").pack()
        e2 = tk.Entry(win)
        e2.pack()
        
        def save():
            self.students.append(Student(e1.get(), e2.get(), "N/A"))
            messagebox.showinfo("Done", "Added")
            win.destroy()
            
        tk.Button(win, text="Add", command=save).pack()

    def exit_app(self):
        t = threading.Thread(target=background_save, args=(self.students, self.courses, self.marks))
        t.start()
        t.join()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagementApp(root)
    root.mainloop()