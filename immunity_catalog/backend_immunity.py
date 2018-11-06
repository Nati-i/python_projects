import sqlite3
import datetime

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS data
        (id INTEGER PRIMARY KEY,
        date text,
        items text)
        """)
        self.cur.execute("""CREATE TABLE IF NOT EXISTS symptoms
        (id INTEGER PRIMARY KEY,
        date text,
        symptoms text)
        """)
        self.conn.commit()
    
    def insert_food(self, date, items):
        self.cur.execute("""INSERT INTO data VALUES
        (NULL,
        ?,
        ?)
        """,(date, items))
        self.conn.commit()
    
    def insert_symptoms(self, date=datetime.date.today(), symptoms=""):
        self.cur.execute("""INSERT INTO symptoms VALUES
        (NULL,
        ?,
        ?)
        """,(date, symptoms))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM data")
        rows = self.cur.fetchall()
        return rows
    
    def view_date(self, date="", items=""):
        self.cur.execute("""
        SELECT * FROM data WHERE date=? OR items=?
        """,(date, items))
        rows = self.cur.fetchall()
        return rows
    
    def update(self, date, items):
        self.cur.execute("""
        UPDATE data SET date=?, items=?
        """,(date, items))
        self.conn.commit()

    def close(self):
        self.conn.close()

# Database("test.db")