# = = = = = = = = = PLANNING = = = = = = = = = 
# The main purpose of this is so teachers can view there students grades they have stored.
# - - - -Table - - - -
# If table doesn't exist make a table

# MENU
# 3 options (Add student,remove student,View ALL student grades, View only one student grade)


# - - - - - - - - Add Student Function - - - - - - - - 
# User needs to input (FIRST NAME, LAST NAME,) to create a account
#       User should not be able to enter numbers
# Creates a student username automatically (First letter of last name, two letters of first name, plus a number that increases)
# Assigns username with @ANSchool.com to create the emai
# Stores all information into the students.db


# - - - - - - - - Remove Student Function - - - - - - - -
# Shows all the students in the database
# Input students first name
#       Checks if it's in database
# Remove student


# - - - - - - - - View Student Function - - - - - - - -
# Show all students in the database
# Input students first name
#       Checks in database
# Shows students grades



import sqlite3
from errorhandling import name_errorhandling,int_errorhandling
class StudentSystem:
        def __init__(self, db_name = "students.db"):
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor() # Runs SQL
            self.create_tables()
            self.counter = 0
        def create_tables(self):
            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS students (
                                studentID TEXT PRIMARY KEY,
                                firstname TEXT,
                                lastname TEXT,
                                email TEXT
                                )
                                """)
            self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS grades (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        studentID TEXT,
                                        course TEXT,
                                        grade TEXT
                                )
                                """)
            self.conn.commit()
        def add_student(self):
                loops = int_errorhandling("How many students will you like to add? ")
                for i in range(loops):
                        self.counter += 1
                        firstname = name_errorhandling("Enter student's first name: ")
                        lastname = name_errorhandling("Enter student's last name: ")
                        studentID = firstname[0].upper() + lastname[:2].upper() + str(self.counter)
                        studentemail = studentID + "@ANSchool.com"
                        datainputted = StudentInformation(firstname,lastname,studentID,studentemail)
                        self.cursor.execute("""
                                            INSERT INTO students (studentID, firstname,lastname,email)
                                            VALUES (?,?,?,?)
                                            """, (studentID,firstname,lastname,studentemail))
                        self.conn.commit()
                        print(f"You have successfully added {firstname} {lastname}")
        def remove_student():
                print("")
        
        def view_students(self):
                while True:
                        print("= = = = = = VIEW STUDENT MENU = = = = = =")
                        print("- - 1) View ALL students (WITHOUT GRADES) - -")
                        print("- - 2) View ALL students (WITH GRADES) - -")
                        print("- - 3) View specific student - -")
                        print("= = = = = = = = = = = = = = = = =")
                        view_choice = int_errorhandling("Enter from 1-2: ")
                        if view_choice == 1:
                                self.cursor.execute("SELECT * FROM students")
                                all_students = self.cursor.fetchall()
                                if not all_students:
                                        print("No students found in database.")
                                        return
                                
                                print("=== ALL STUDENTS ===")
                                for student in all_students:
                                        print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Email: {student[3]}")
                        elif view_choice == 2:
                                print("")
class StudentInformation:
        def __init__(self,firstname,lastname,studentID,studentemail):
                self.firstname = firstname
                self.lastname = lastname
                self.studentID = studentID
                self.studentemail = studentemail

studentsystem = StudentSystem()

studentsystem.view_students()