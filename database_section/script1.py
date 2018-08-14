'''
1. Connect to a database
2. Create a cursor object
3. Write an SQL query
4. Commit changes
5. Close database connection
'''

import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #sql code
    conn.commit()

    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()


update(8,3,"Water Glass")
print(view())
