# NAMA   : FERLI
# NIM    : 210511140
# KELAS  : 21TI D

class Komputer:
    def __init__(self, merek):
        self.merek = merek

    def tampil_merek(self):
        print("Merek: ", self.merek)


class Desktop(Komputer):
    def tampil_spesifikasi(self):
        print("Spesifikasi: Desktop")

    def tampil_merek(self):
        print("Merek Desktop: ", self.merek)


class Laptop(Komputer):
    def tampil_spesifikasi(self):
        print("Spesifikasi: Laptop")

    def tampil_merek(self):
        print("Merek Laptop: ", self.merek)


def tampilkan_info(komputer):
    komputer.tampil_merek()
    komputer.tampil_spesifikasi()


komputer1 = Desktop("Lenovo")
komputer2 = Laptop("Asus")

tampilkan_info(komputer1)
tampilkan_info(komputer2)
