# NAMA   : FERLI
# NIM    : 210511140
# KELAS  : 21TI D

from abc import ABC, abstractmethod

class Buah(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def tampil_info(self):
        pass

class Apel(Buah):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def tampil_info(self):
        print("Nama: ", self.nama)
        print("Warna: ", self.warna)
        print("Rasa: Manis")

class Jeruk(Buah):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis

    def tampil_info(self):
        print("Nama: ", self.nama)
        print("Jenis: ", self.jenis)
        print("Rasa: Asam")

def tampilkan_info_buah(buah):
    buah.tampil_info()

buah1 = Apel("Apel Malang", "Merah")
buah2 = Jeruk("Jeruk Bali", "Mandarin")

tampilkan_info_buah(buah1)
tampilkan_info_buah(buah2)
