class Pekerjaan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def info_pekerjaan(self):
        print("Nama pekerjaan:", self.nama)
        print("Gaji:", self.gaji)

class Karyawan(Pekerjaan):
    def __init__(self, nama, gaji, jabatan):
        self.jabatan = jabatan

    def info_karyawan(self):
        super().info_pekerjaan()
        print("Jabatan:", self.jabatan)

class Manager(Pekerjaan):
    def __init__(self, nama, gaji, departemen):
        super().__init__(nama, gaji)
        self.departemen = departemen

    def info_manager(self):
        super().info_pekerjaan()
        print("Departemen:", self.departemen)

class Supervisor(Karyawan, Manager):
    def __init__(self, nama, gaji, jabatan, departemen, wilayah):
        Karyawan.__init__(self, nama, gaji, jabatan)
        Manager.__init__(self, nama, gaji, departemen)
        self.wilayah = wilayah

    def info_supervisor(self):
        super().info_karyawan()
        super().info_manager()
        print("Wilayah:", self.wilayah)

supervisor = Supervisor("John", 5000000, "Supervisor", "Finance", "Jakarta")
supervisor.info_supervisor()
