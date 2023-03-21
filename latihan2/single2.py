class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang belajar.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIM {self.nip} sedang belajar.")

dosenA = Dosen("Ferli", 35, "210511140")
dosenA.berbicara()
dosenA.mengajar() 