# NAMA  : FERLI
# NIM   : 210511140
# KELAS : TI21 D

class Peneliti:
    def __init__(self, nama, institusi):
        self.nama = nama
        self.institusi = institusi
        self.jurnal = Jurnal()

    def submit_artikel(self, judul, isi):
        self.jurnal.tambah_artikel(judul, isi)

class Jurnal:
    def __init__(self):
        self.artikel = []

    def tambah_artikel(self, judul, isi):
        self.artikel.append(Artikel(judul, isi))

class Artikel:
    def __init__(self, judul, isi):
        self.judul = judul
        self.isi = isi

# membuat objek Peneliti
peneliti = Peneliti("Ferli", "Universitas Muhammadiyah Cirebon")

# menambahkan artikel ke jurnal
peneliti.submit_artikel("Judul Artikel 1", "Ini adalah isi dari artikel 1")
peneliti.submit_artikel("Judul Artikel 2", "Ini adalah isi dari artikel 2")

# menampilkan daftar artikel pada jurnal
for artikel in peneliti.jurnal.artikel:
    print(artikel.judul)
    print(artikel.isi)
    print()
