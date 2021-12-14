-- Buat tabel --
CREATE TABLE IF NOT EXISTS alamat(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT, 
    phone_number TEXT);

INSERT INTO alamat (id, first_name, phone_number) VALUES (1, "John Doe", "0822123");

INSERT INTO alamat (id, first_name, phone_number) VALUES (2, "Andrea Wu", "0812345");

INSERT INTO alamat (first_name, phone_number) VALUES ("Andreu Wu", "0822123");