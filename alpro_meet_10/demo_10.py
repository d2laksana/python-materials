import sqlite3

# Init Database
with sqlite3.connect("telepon.db") as db:
    cursor = db.cursor()

# Membuat Tabel
query1 = '''CREATE TABLE IF NOT EXISTS alamat(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT, 
    phone_number TEXT);'''
cursor.execute(query1)

# Insert data
# query2 = '''INSERT INTO alamat (id, first_name, phone_number) VALUES (1, "John Doe", "0822123")'''
# cursor.execute(query2)
# db.commit()

# query3 = '''INSERT INTO alamat (id, first_name, phone_number) VALUES (2, "Andrea Wu", "0812345")'''
# cursor.execute(query3)
# db.commit()

# query4 = '''INSERT INTO alamat (id, first_name, phone_number) VALUES (3, "Tylor Cruwe", "0854321")'''
# cursor.execute(query4)
# db.commit()

# query5 = '''INSERT INTO alamat (first_name, phone_number) 
#     VALUES ("Peter Friese", "0855321")'''
# cursor.execute(query5)
# db.commit()


# Menampilkan data dari database
query6 = '''SELECT * FROM alamat'''
cursor.execute(query6)

for baris in cursor.fetchall():
    print(baris)


# Close connection from database
db.close()