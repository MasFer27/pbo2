class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def tampilkan_profil(self):
        print("Nama:", self.nama)
        print("Gaji:", self.gaji)


class Manajer(Pegawai):
    def __init__(self, nama, gaji, departemen):
        super().__init__(nama, gaji)
        self.departemen = departemen

    def tampilkan_profil(self):
        super().tampilkan_profil()
        print("Departemen:", self.departemen)


class Programmer(Pegawai):
    def __init__(self, nama, gaji, bahasa_pemrograman):
        super().__init__(nama, gaji)
        self.bahasa_pemrograman = bahasa_pemrograman

    def tampilkan_profil(self):
        super().tampilkan_profil()
        print("Bahasa Pemrograman:", self.bahasa_pemrograman)


# Contoh penggunaan kelas-kelas di atas:
pegawai1 = Pegawai("Andi", 5000000)
pegawai1.tampilkan_profil()

manajer1 = Manajer("Budi", 10000000, "IT")
manajer1.tampilkan_profil()

programmer1 = Programmer("Cici", 7500000, "Python")
programmer1.tampilkan_profil()
