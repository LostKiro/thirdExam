import sqlite3

db = sqlite3.connect('bace2.db')
cursor = db.cursor()

cursor.execute('CREATE TABLE my_table(id INTEGER PRIMARY KEY, name TEXT,surname TEXT, age INTEGER);')
cursor.execute('INSERT INTO my_table (name,surname, age) VALUES ("Petya","Pupkin", 11),'
               ' ("Pasha","Morozov", 32),'
               ' ("Gena","Bukin", 19);')

db.commit()
cursor.close()
db.close()


