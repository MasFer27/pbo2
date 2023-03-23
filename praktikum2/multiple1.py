class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis
    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")
class Reptil(Hewan):
    def __init__(self, jenis, nama):
        self.nama = nama
    def display_info(self):
        super().display_info()
        print(f"Nama mamalia: {self.nama}")
class Karnivora(Hewan):
    def __init__(self, jenis, makanan):
        super().__init__(jenis)
        self.makanan = makanan
    def display_info(self):
        super().display_info()
        print(f"Jenis makanan: {self.makanan}")

class Buaya(Reptil, Karnivora):
    def __init__(self, jenis, nama, makanan):
        Reptil.__init__(self, jenis, nama)
        Karnivora.__init__(self, jenis, makanan)
    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")
# contoh penggunaan
buayaA = Buaya("Reptil", "Buaya Sumatera", "Daging")
buayaA.display_info()