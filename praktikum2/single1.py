class Buah:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    def manis(self):
        print(f"buah {self.nama} rasanya manis")

class Semangka(Buah):
    def __init__(self, nama, warna):
        super().__init__(nama, warna)
    def daging(self):
        print(f"buah {self.nama} warnanya {self.warna}")
        
SemangkaA = Semangka("Semangka", "Hijau")
SemangkaA.manis()
SemangkaA.daging()