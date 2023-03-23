class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print(f"Saya mempunyai {self.jenis} {self.merk} berwarna {self.warna}")

class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, ):
        super().__init__(jenis, merk, warna)
    def belok(self):
        print(f"{self.jenis} ini sedang belok.")

motorA = Mobil("Mobil", "Rubicon", "Putih")
motorA.berkendara()
motorA.belok() 