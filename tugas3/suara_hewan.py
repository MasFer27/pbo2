import pygame

class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "suara_kucing.mp3"

class Anjing(Hewan):
    def suara(self):
        return "suara_anjing.mp3"

class Ayam(Hewan):
    def suara(self):
        return "suara_ayam.mp3"

class Burung(Hewan):
    def suara(self):
        return "suara_burung.mp3"

class Kambing(Hewan):
    def suara(self):
        return "suara_kambing.mp3"

class Gajah(Hewan):
    def suara(self):
        return "suara_gajah.mp3"

class Kuda(Hewan):
    def suara(self):
        return "suara_kuda.mp3"

class Sapi(Hewan):
    def suara(self):
        return "suara_sapi.mp3"

class Singa(Hewan):
    def suara(self):
        return "suara_singa.mp3"

# Membuat objek dari setiap kelas
hewan1 = Kucing()
hewan2 = Anjing()
hewan3 = Ayam()
hewan4 = Burung()
hewan5 = Kambing()
hewan6 = Gajah()
hewan7 = Kuda()
hewan8 = Sapi()
hewan9 = Singa()

# Inisialisasi Pygame mixer
pygame.mixer.init()

# Memanggil metode suara() dan memutar file MP3-nya
for hewan in [hewan1, hewan2, hewan3, hewan4, hewan5, hewan6, hewan7, hewan8, hewan9]:
    suara_file = hewan.suara()
    pygame.mixer.music.load(suara_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
