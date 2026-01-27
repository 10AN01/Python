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
                        
class StudentInformation:
        def __init__(self,firstname,lastname,studentID,studentemail):
                self.firstname = firstname
                self.lastname = lastname
                self.studentID = studentID
                self.studentemail = studentemail

studentsystem = StudentSystem()
studentsystem.add_student()