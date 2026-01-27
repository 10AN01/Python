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
import random
from errorhandling import name_errorhandling,int_errorhandling
class StudentSystem:
        def __init__(self, db_name = "students.db"):
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor() # Runs SQL
            self.create_tables()
        def create_tables(self):
                self.cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS student(
                                            studentIdIncrement INTEGER PRIMARY KEY AUTOINCREMENT,
                                            studentID TEXT,
                                            firstname TEXT,
                                            lastname TEXT,
                                            email TEXT
                                    )
                                    """)
                self.cursor.execute ("""
                                     CREATE TABLE IF NOT EXISTS grades(
                                             studentIdIncrement INTEGER PRIMARY KEY AUTOINCREMENT,
                                             studentID TEXT,
                                             grades INTEGER,
                                             subject TEXT
                                     )
                                     
                                     """)
                self.conn.commit()
        def add_student(self):
                print("="* 21)
                print("     ADD STUDENT")
                print("="* 21)
                loops = int_errorhandling("Enter how many students you'll like to add: ")
                for i in range(loops):
                        firstname = name_errorhandling("Enter student's first name: ")
                        lastname = name_errorhandling("Enter student's last name: ")
                        end_studentID = str(random.randint(1000,9999))
                        studentID = firstname[0] + lastname[:2] + end_studentID
                        studentemail = studentID + "@ANSchool.com"
# Enters data just inputted into the columns
                        self.cursor.execute("""
                                            INSERT INTO student (studentIdIncrement,studentID,firstname,lastname,email)
                                            VALUES (NULL,?,?,?,?)
                                            """, (studentID,firstname,lastname,studentemail))
# conn.commit makes the action permanentS
                        self.conn.commit()
        def remove_student(self):
                print("="* 25)
                print("     ALL STUDENT")
                print("="* 25)
# Select everything in the database (Can see everything)
                self.cursor.execute("SELECT * FROM student")
                all_student = self.cursor.fetchall()
# loops depending on how much data there is
                for student in all_student:
                        print(f"Student ID: {student[1]}\nFirst Name: {student[2]}\nLast Name: {student[3]} \nEmail: {student[4]}")
                        print("-"*24)
# Will get only one data that is selected.
                studentID_Remove = input("Enter the student ID to remove: ")
                student = self.cursor.fetchone()
# If the student ID is found then delete
                if student is not None:
                        self.cursor.execute("DELETE FROM student WHERE studentID = ?",(studentID_Remove,))
                        self.conn.commit()
                        print("Student removed successfully!")
                else:
                        print("No student found with that ID")
                        return
        def add_grades(self):
                print("ADD GRADE")
# Select everything in the database (Can see everything)
                self.cursor.execute("SELECT * FROM student")
                all_student = self.cursor.fetchall()
# loops depending on how much data there is
                for student in all_student:
                        print(f"Student ID: {student[1]}\nFirst Name: {student[2]}\nLast Name: {student[3]} \nEmail: {student[4]}")
                        print("-"*24)
                Student_ID = input("Enter the students ID: ")
                self.cursor.execute("""
                                    SELECT * FROM student WHERE studentID = ?""",(Student_ID,)
                                    )
                
                student = self.cursor.fetchone()
                if student is not None:
                        while True:
                                grade = int_errorhandling("Enter the student's grade: ")
                                if grade >= 0 and grade <=9:
                                        break
                                else:
                                        print("Invalid grade. Needs to between from 1 to 9[")
                        while True:
                                print("Subjects")
                                print("1) Computer Science")
                                print("2) Math")
                                print("3) English")
                                print("4) Science")
                                print("5) History")
                                print("6) Art")
                                print("7) Physical Education")
                                print("8) Music")
                                print("9) Geography")
                                print("10) Social Studies")
                                choice = int_errorhandling("Enter the subject number: ")
                                if choice == 1:
                                        subject = "Computer Science"
                                        break
                                elif choice == 2:
                                        subject = "Math"
                                        break
                                elif choice == 3:
                                        subject = "English"
                                        break
                                elif choice == 4:
                                        subject = "Science"
                                        break
                                elif choice == 5:
                                        subject = "History"
                                        break
                                elif choice == 6:
                                        subject = "Art"
                                        break
                                elif choice == 7:
                                        subject = "Physical Education"
                                        break
                                elif choice == 8:
                                        subject = "Music"
                                        break
                                elif choice == 9:
                                        subject = "Geography"
                                        break
                                elif choice == 10:
                                        subject = "Social Studies"
                                        break
                                else:
                                        print("Invalid choice")

                else:
                        print("Student not found.")
                        return
                self.cursor.execute("""
                                    INSERT INTO grades (studentIdIncrement,studentID,grades,subject)
                                    VALUES (NULL,?,?,?)
                                    """, (Student_ID,grade,subject))
                self.conn.commit()

                        
                        
class StudentInformation:
        def __init__(self,firstname,lastname,studentID,studentemail):
                self.firstname = firstname
                self.lastname = lastname
                self.studentID = studentID
                self.studentemail = studentemail

studentsystem = StudentSystem()
studentsystem.add_grades()