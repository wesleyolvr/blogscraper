import sqlite3

con = sqlite3.connect('mynews.db')
cur = con.cursor()
sql = """
CREATE TABLE news (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Title Text NOT NULL UNIQUE)
""" 
cur.execute(sql)
con.commit()
con.close()
