class Buah:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    
    def dipanen(self):
        print(f"{self.nama} telah dipanen.")
    
    def disimpan(self):
        print(f"{self.nama} sedang disimpan di rak pendingin.")

    def __str__(self):
        return f"{self.nama} ({self.warna})"

class BuahBerbiji(Buah):
    def __init__(self, nama, warna, biji):
        super().__init__(nama, warna)
        self.biji = biji
    
    def dibuat_jus(self):
        print(f"{self.nama} ({self.warna}) diblender menjadi jus...")
    
    def dikupas(self):
        print(f"Mengupas {self.nama} ({self.warna}) dan mengambil bijinya...")

class BuahBerpelir(Buah):
    def __init__(self, nama, warna, is_manis):
        super().__init__(nama, warna)
        self.is_manis = is_manis
    
    def dikupas(self):
        print(f"Mengupas {self.nama} ({self.warna}) dan memotongnya menjadi potongan kecil...")
    
    def dimakan_langsung(self):
        if self.is_manis:
            print(f"Rasanya manis sekali!")
        else:
            print(f"Rasanya asam sekali...")

# contoh penggunaan
jeruk = BuahBerpelir("Jeruk", "Orange", True)
print(jeruk)
jeruk.dikupas()
jeruk.dimakan_langsung()
