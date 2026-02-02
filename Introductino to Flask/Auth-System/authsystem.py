
from dbm import sqlite3
class AuthSystem:
    def __init__(self):
        self.conn = sqlite3.connect("accounts.db")
        self.cursor = self.conn.cursor() # Runs SQL
        self.execute("""
                     CREATE TABLE IF NOT EXIST accounts(
                         
                     )
                     """)
    def register_user(self):
        
    def login_user(self):
        