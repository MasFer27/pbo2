class Binatang:
    def __init__(self, nama):
        self.nama = nama
        
    def bersuara(self):
        print("Bersuara...")

class Hewan(Binatang):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
        
    def gerak(self):
        print("Bergerak...")
        
class Mamalia(Hewan):
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis)
        self.habitat = habitat
        
    def menyusui(self):
        print("Menyusui anaknya...")

class Burung(Hewan):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna
        
    def terbang(self):
        print("Terbang tinggi...")
        
class Ayam(Burung, Binatang):
    def __init__(self, nama, jenis, warna, habitat):
        Binatang.__init__(self, nama)
        Hewan.__init__(self, nama, jenis)
        Burung.__init__(self, nama, jenis, warna)
        self.habitat = habitat
        
    def bersuara(self):
        print(f"{self.nama} {self.jenis} bunyinya Kukuruyuk...")
        
    def berlari(self):
        print(f"{self.nama} {self.jenis} Berlari cepat...")

ayam = Ayam("Ayam", "Cemani", "hitam", "darat")
ayam.bersuara()
ayam.berlari()