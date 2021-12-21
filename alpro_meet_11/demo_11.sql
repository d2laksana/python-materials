-- Menghapus tabel dari database
DROP TABLE IF EXISTS `mahasiswa`;

-- Membuat tabel
CREATE TABLE IF NOT EXISTS `mahasiswa` (
	`npm` INTEGER PRIMARY KEY AUTOINCREMENT,
	`nama` TEXT,
	`jenis_kelamin` TEXT,
	`jenis_sekolah` CHAR,
	`status_sekolah` CHAR,
	`ipk_semester_1` REAL,
	`ipk_semester_2` REAL
);
--`rata_rata_ipk` AS ((`ipk_semester_1` + `ipk_semester_2`) / 2) VIRTUAL

SELECT * FROM `mahasiswa`;

SELECT * FROM `mahasiswa` WHERE `mahasiswa`.`rata_rata_ipk` > 3.00;

-- Rata-rata keseluruhan
SELECT avg(`mahasiswa`.`rata_rata_ipk`) as rata_rata_kelas FROM `mahasiswa`;

-- Menambahkan data ke tabel
INSERT INTO `mahasiswa` VALUES ('521001', 'Budi Setiawan', 'L', 'SMA', 'N', 2.60, 3.90);

-- Insert batch -> lebih dari 1 -> Insert Batch
INSERT INTO `mahasiswa` (`nama`, `jenis_kelamin`, `jenis_sekolah`, `status_sekolah`, `ipk_semester_1`, `ipk_semester_2`) VALUES
('Joni Hermawan', 'L', 'SMA', 'N', 2.99, 3.30),
('Endah Sulastri', 'P', 'SMA', 'N', 3.56, 2.90),
('Akmal Laksmana', 'L', 'SMA', 'S', 3.25, 3.45),
('Nugroho', 'L', 'SMK', 'N', 2.75, 3.15),
('Rini Nuraeni', 'P', 'SMA', 'N', 2.85, 2.9),
('Farida', 'P', 'SMK', 'S', 3.81, 3.60);

-- Update data berdasarkan PRIMARY KEY
UPDATE <nama_tabel> SET <nama_kolom> = <nilai baru>, ... WHERE <kondisi>;

UPDATE `mahasiswa` SET `ipk_semester_2` = 3.00;

UPDATE `mahasiswa` SET `ipk_semester_2` = 3.25 WHERE ipk_semester_2 < 3.00;

UPDATE `mahasiswa` SET `ipk_semester_1` = 3.25 WHERE status_sekolah = 'S';

UPDATE `mahasiswa` SET `ipk_semester_2` = 3.25 WHERE nama = 'Joni Hermawan';

UPDATE mahasiswa SET nama = 'Adi Nugroho', jenis_sekolah = 'SMA' WHERE npm = 521005;

-- Tambah Kolom
ALTER TABLE mahasiswa ADD alamat TEXT;

-- Delete data
-- Hapus semua data dari tabel
DELETE FROM <nama_tabel>;

DELETE FROM mahasiswa;

-- Hapus data dengan kondisi
DELETE FROM <nama_tabel> WHERE <kondisi>;

DELETE FROM mahasiswa WHERE npm = 521011;

DELETE from mahasiswa 
WHERE ipk_semester_1 < 3.00
OR ipk_semester_2 < 3.00;
