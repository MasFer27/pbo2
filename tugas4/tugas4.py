# NAMA  : FERLI
# NIM   : 210511140
# KELAS : TI21 D

class Mesin:
    def __init__(self, tipe, cc):
        self.tipe = tipe
        self.cc = cc

class Mobil:
    def __init__(self, merek, model, mesin):
        self.merek = merek
        self.model = model
        self.mesin = mesin

    def __str__(self):
        return f"{self.merek} {self.model}"

mesin1 = Mesin("Bensin", 1500)
mobil1 = Mobil("Toyota", "Avanza", mesin1)

mesin2 = Mesin("Diesel", 2000)
mobil2 = Mobil("Mitsubishi", "Pajero Sport", mesin2)

print(mobil1) # output: Toyota Avanza
print(mobil1.mesin.tipe) # output: Bensin
print(mobil2.mesin.cc) # output: 2000
