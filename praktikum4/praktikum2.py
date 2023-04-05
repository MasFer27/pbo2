# NAMA  : FERLI
# NIM   : 210511140
# KELAS : TI21 D

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok_kkm = Kelompok_KKM()

    def ambil_mata_kuliah(self, mata_kuliah):
        self.kelompok_kkm.tambah_mata_kuliah(mata_kuliah)

class Kelompok_KKM:
    def __init__(self):
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah.append(mata_kuliah)

# membuat objek Mahasiswa
mahasiswa = Mahasiswa("FERLI", "210511140")

# menambahkan mata kuliah
mahasiswa.ambil_mata_kuliah("Matematika Diskrit")
mahasiswa.ambil_mata_kuliah("Algoritma Pemrograman")

# menampilkan daftar mata kuliah yang diambil oleh mahasiswa
for mata_kuliah in mahasiswa.kelompok_kkm.mata_kuliah:
    print(mata_kuliah)
