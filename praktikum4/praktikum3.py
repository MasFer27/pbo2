# NAMA  : FERLI
# NIM   : 210511140
# KELAS : TI21 D

class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tulis_buku(self, judul):
        buku = Buku(judul)
        self.buku.append(buku)
        return buku

class Buku:
    def __init__(self, judul):
        self.judul = judul

    def __str__(self):
        return self.judul

# membuat objek Penulis
penulis = Penulis("FERLI")

# menulis dua buku baru
buku1 = penulis.tulis_buku("Laskar Pelangi")
buku2 = penulis.tulis_buku("Berbicara Itu Ada Seninya")

# menampilkan daftar buku yang ditulis oleh penulis
for buku in penulis.buku:
    print(buku)
