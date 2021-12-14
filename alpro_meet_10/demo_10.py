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

# Menampilkan data dari database
query2 = '''SELECT first_name, phone_number FROM alamat'''
cursor.execute(query2)

for baris in cursor.fetchall():
    print(baris)


# Close connection from database
db.close()