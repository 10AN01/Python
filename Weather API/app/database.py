import sqlite3

conn = sqlite3.connect("weather.db",check_same_thread=False)
cursor = conn.cursor()
# Create table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS weather(
                   city TEXT PRIMARY KEY,
                   Temperature REAL,
                   description TEXT
               )
               """)
conn.commit()

# Insert Data into the table.
def save_weather(city,temperature,description):
    cursor.execute("""
    INSERT INTO weather(city,temperature,description)
    VALUES (?,?,?)
    """,(city,temperature,description)
    )
    conn.commit()
    
def check_city_exist(city):
    cursor.execute("""
                   SELECT * FROM weather WHERE city = ?
                   """,(city,))
    result = cursor.fetchone()
    return result