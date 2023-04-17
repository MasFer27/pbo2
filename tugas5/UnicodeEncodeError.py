#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

try:
    # Potongan kode yang mungkin menimbulkan UnicodeEncodeError
    data = "Contoh teks dengan karakter non-ASCII: àáâ"
    encoded_data = data.encode('ascii')
    print(encoded_data)
except UnicodeEncodeError:
    # Tangani kesalahan di sini
    print("Kesalahan: karakter non-ASCII tidak dapat diencode sebagai ASCII")
