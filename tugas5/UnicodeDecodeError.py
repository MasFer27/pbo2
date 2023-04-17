#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # Potongan kode yang mungkin menimbulkan UnicodeDecodeError
    file = open("teks.txt", "r", encoding="utf-8")
    data = file.read()
    file.close()
    print(data)
except UnicodeDecodeError:
    # Tangani kesalahan di sini
    print("Kesalahan: File tidak dalam format UTF-8")
