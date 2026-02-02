# FUNCTIONS

# ACCOUNT FUNCTIONS
# - - - - - - - - - - - -
# Add account
#   . User must be able to first/last name, email, password
# Remove account
#   . User needs the password to remove the account
# Login
#   . User needs the email and password to login
#   . Depending on what role the user has is what it can do

# BUG FUNCTIONS
# - - - - - - - - - - - - -
# Add a bug report
#   . Must give a list of bugs, user must pick from those bugs.
#   . Give a comment on the bug
#   . Must be assigned to that user.
# Search for specific bug (Admin/Dev role)
#   . Can view at all bugs/reports and give comments (Search for specific bug report)
#   . Should be able to close the ticket and update the status
from errorhandling import str_errorhandling,email_errorhandling,password_length
import sqlite3
import random
import bcrypt
class UserInformation():
    def __init__(self,userid,firstname,lastname,email,password,role):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
        
class BugSystem():
    def __init__(self,):
        self.conn = sqlite3.connect("accounts.db")
        self.cursor = self.conn.cursor() # Runs SQL
        self.cursor.execute ("""
                            CREATE TABLE IF NOT EXISTS accounts(
                                UserIDIncrements INTEGER PRIMARY KEY AUTOINCREMENT,
                                UserID TEXT,
                                First_Name TEXT,
                                Last_Name TEXT,
                                Email TEXT,
                                Password TEXT,
                                User_Role TEXT
                            )
                            """)
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS reports(
                                ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
                                UserID TEXT,
                                Bug_Subject TEXT,
                                Comment TEXT,
                                Status TEXT,
                                Created At TEXT DEFAULT CURRENT_TIMESTAMP
                            )
                            """)
        self.conn.commit()
    def add_account(self):
        print("="*25)
        print("       ADD ACCOUNT")
        print("="*25)
        firstname = str_errorhandling("Enter first name:")
        lastname = str_errorhandling("Enter last name: ")
        str_number = str(random.randint(1000,9999))
        userid = firstname[0] + lastname[:2] + str_number
        email = email_errorhandling("Enter in your email: ")
        password = password_length("Enter a password: ")
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        role = "User"
        datainputted = UserInformation(userid,firstname,lastname,email,hashed_pw,role)
        self.cursor.execute("""
                            INSERT INTO accounts (UserID,First_Name,Last_Name,Email,Password,User_Role)
                            VALUES (?,?,?,?,?,?)
                            
                            """, (
                            datainputted.userid,
                            datainputted.firstname,
                            datainputted.lastname,
                            datainputted.email,
                            datainputted.hashed_pw,
                            datainputted.role
                            ))
        self.conn.commit()
    def remove_account(self):
        print("="*25)
        print("       REMOVE ACCOUNT")
        print("="*25)
        email_input = input("Enter the email of the account you'll like to remove: ")
        self.cursor.execute("""
                            SELECT * FROM accounts WHERE Email = ?
                            """,(email_input,))
        email_selected = self.cursor.fetchone()
        if email_selected is not None:
            if email_selected[4] == email_input:
                password_input = input("Enter password:")
                self.cursor.execute("""
                                    SELECT * FROM accounts WHERE Password = ?
                                    """,(password_input,))
                password_selected = self.cursor.fetchone()
                if password_selected is not None:
                    stored_hash = password_selected[5]
                    if bcrypt.checkpw(password_selected.encode(), stored_hash.encode()):
                        self.cursor.execute("""
                                            DELETE FROM accounts WHERE password = ?
                                            """,(stored_hash,))
                    else:
                        print("Invalid Password")
                        return
        else:
            print("Invalid Email")
            return
        self.conn.commit()
            
bugsystem= BugSystem()
bugsystem.remove_account()
